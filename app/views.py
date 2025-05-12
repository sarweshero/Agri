from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.urls import reverse
import uuid
import qrcode
import base64
from io import BytesIO
from icecream import ic
from django.views.decorators.csrf import csrf_exempt  # added import

# Create your views here.

import json
import uuid
import base64
import qrcode
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from icecream import ic # Assuming you are using icecream for debugging

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

            ic(data) # Use icecream to inspect the parsed data dictionary

            # Store the parsed data dictionary in the session with a UUID key
            data_id = str(uuid.uuid4())
            request.session[data_id] = data # Store the parsed dictionary
            request.session.save()  # ensure session data is persisted

            # Build URL to display_data view (make sure 'display_data' URL pattern is defined)
            # You might need to adjust how you build the absolute URL based on your setup
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
            ic(f"An unexpected error occurred: {e}") # Log the unexpected error
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse("Only POST method is allowed", status=405)
    
def display_data(request, data_id):
    data = request.session.get(data_id, None)  # use None as a default
    if data is None:
        raise Http404("Data not found")
    return render(request, 'display_data.html', {'data': data})
