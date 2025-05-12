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

@csrf_exempt  # added decorator to bypass CSRF for POST requests
def generate_qr(request):
    if request.method == 'POST':
        try:
            # Retrieve form data and store in session with a UUID key
            ic(request.POST)
            ic(request.data)
            form_data = ic(request.POST.dict())
            
            data_id = str(uuid.uuid4())
            request.session[data_id] = form_data
            request.session.save()  # ensure session data is persisted

            # Build URL to display_data view
            url = request.build_absolute_uri(reverse('display_data', args=[data_id]))

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
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return HttpResponse("Only POST method is allowed", status=405)

def display_data(request, data_id):
    data = request.session.get(data_id, None)  # use None as a default
    if data is None:
        raise Http404("Data not found")
    return render(request, 'display_data.html', {'data': data})
