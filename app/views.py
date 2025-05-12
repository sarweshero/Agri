import json
import uuid
import base64
import qrcode
from io import BytesIO
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.base import ContentFile
import datetime
from django.core.cache import cache
from icecream import ic
from .models import * 


@api_view(['POST'])
def create_landprep(request):
    data = request.data.copy()

    # Map frontend fields to model fields
    date_str = data.get('selectedDate')
    fertilizer = data.get('fertilizer')
    quantity = data.get('quantity')
    photo_base64s = data.get('photoBase64s', [])

    # Convert date string to date object
    try:
        date = datetime.datetime.fromisoformat(date_str).date()
    except Exception as e:
        return Response({'error': f'Invalid date format: {e}'}, status=status.HTTP_400_BAD_REQUEST)

    # Use only the first photo (if multiple)
    photo_file = None
    if photo_base64s and isinstance(photo_base64s, list):
        try:
            photo_data = photo_base64s[0]
            format, imgstr = 'jpeg', photo_data
            file_name = f'landprep_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.jpg'
            photo_file = ContentFile(base64.b64decode(imgstr), name=file_name)
        except Exception as e:
            return Response({'error': f'Invalid image data: {e}'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        landprep_instance = landprep.objects.create(
            date=date,
            fertilizer=fertilizer,
            quantity=int(quantity),
            photo=photo_file
        )
        return Response({
            'message': 'LandPrep instance created successfully',
            'id': landprep_instance.id
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@csrf_exempt
def generate_qr(request):
    if request.method == 'POST':
        try:
            # Read the raw request body
            raw_body = request.body

            # Decode the bytes to a string and parse the JSON
            try:
                data = json.loads(raw_body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON received'}, status=400)

            # ic(data)  # Use icecream to inspect the parsed data dictionary

            # Generate a UUID key and store the parsed data in the cache (shared storage)
            data_id = str(uuid.uuid4())
            cache.set(data_id, data)

            # Build URL to display_data view (make sure 'display_data' URL pattern is defined)
            try:
                url = request.build_absolute_uri(reverse('display_data', args=[data_id]))
            except Exception as url_error:
                # Handle potential errors if the 'display_data' URL name doesn't exist
                print(f"Error reversing URL 'display_data': {url_error}")
                return JsonResponse({'error': 'Backend URL configuration error'}, status=500)

            # Generate QR code with given parameters
            qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=4
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Convert QR code image to base64
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            return JsonResponse({'url': url, 'qr_code': img_str})
        except Exception as e:
            # Catch any other unexpected errors during processing
            ic(f"An unexpected error occurred: {e}")  # Log the unexpected error
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse("Only POST method is allowed", status=405)
    
def display_data(request, data_id):
    data = cache.get(data_id)  # Retrieve data from cache instead of session
    if data is None:
        raise Http404("Data not found")
    return render(request, 'display_data.html', {'data': data})
