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
from icecream import ic
from django.core.cache import cache  # New import for shared storage
from icecream import ic  # Assuming you are using icecream for debugging
from .models import *  # Import your models including LandPrep
@api_view(['POST'])
def create_landprep(request):
    # Make a mutable copy of the incoming data
    data = request.data.copy()
    
    # If your model has an image field (e.g., 'photo'), handle the uploaded image:
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    
    # Fetch the 'id' from query parameters and remap it to 'belong_to'
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for LandPrep: {data}")
    try:
        # Create the LandPrep instance using the provided data and image (if any)
        landprep_instance = landprep.objects.create(**data)
        return Response({
            'message': 'LandPrep instance created successfully',
            'id': landprep_instance.id
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        ic(f"Error creating LandPrep instance: {e}")
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
