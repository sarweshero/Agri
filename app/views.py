# @csrf_exempt
# def generate_qr(request):
#     if request.method == 'POST':
#         try:
#             # Read the raw request body
#             raw_body = request.body

#             # Decode the bytes to a string and parse the JSON
#             try:
#                 data = json.loads(raw_body.decode('utf-8'))
#             except json.JSONDecodeError:
#                 return JsonResponse({'error': 'Invalid JSON received'}, status=400)

#             # ic(data)  # Use icecream to inspect the parsed data dictionary

#             # Generate a UUID key and store the parsed data in the cache (shared storage)
#             data_id = str(uuid.uuid4())
#             cache.set(data_id, data)

#             # Build URL to display_data view (make sure 'display_data' URL pattern is defined)
#             try:
#                 url = request.build_absolute_uri(reverse('display_data', args=[data_id]))
#             except Exception as url_error:
#                 # Handle potential errors if the 'display_data' URL name doesn't exist
#                 print(f"Error reversing URL 'display_data': {url_error}")
#                 return JsonResponse({'error': 'Backend URL configuration error'}, status=500)

#             # Generate QR code with given parameters
#             qr = qrcode.QRCode(
#                 version=1,
#                 box_size=10,
#                 border=4
#             )
#             qr.add_data(url)
#             qr.make(fit=True)
#             img = qr.make_image(fill_color="black", back_color="white")

#             # Convert QR code image to base64
#             buffered = BytesIO()
#             img.save(buffered, format="PNG")
#             img_str = base64.b64encode(buffered.getvalue()).decode()

#             return JsonResponse({'url': url, 'qr_code': img_str})
#         except Exception as e:
#             # Catch any other unexpected errors during processing
#             ic(f"An unexpected error occurred: {e}")  # Log the unexpected error
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return HttpResponse("Only POST method is allowed", status=405)
    
# def display_data(request, data_id):
#     data = cache.get(data_id)  # Retrieve data from cache instead of session
#     if data is None:
#         raise Http404("Data not found")
#     return render(request, 'display_data.html', {'data': data})
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
from .serializers import (
    LandPrepSerializer,
    TransplantingSerializer,
    FertilizerSerializer,
    HarverstSerializer,
    PackagingSerializer,
    ProcurementSerializer,
    PackingSerializer
)

@api_view(['POST'])
def create_landprep(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for LandPrep: {data}")
    serializer = LandPrepSerializer(data=data)
    if serializer.is_valid():
        landprep_instance = serializer.save()
        return Response({
            'message': 'LandPrep instance created successfully',
            'id': landprep_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def create_transplanting(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for Transplanting: {data}")
    serializer = TransplantingSerializer(data=data)
    if serializer.is_valid():
        transplanting_instance = serializer.save()
        return Response({
            'message': 'Transplanting instance created successfully',
            'id': transplanting_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_fertilizer(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for Fertilizer: {data}")
    serializer = FertilizerSerializer(data=data)
    if serializer.is_valid():
        fertilizer_instance = serializer.save()
        return Response({
            'message': 'Fertilizer instance created successfully',
            'id': fertilizer_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_harverst(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for Harverst: {data}")
    serializer = HarverstSerializer(data=data)
    if serializer.is_valid():
        harverst_instance = serializer.save()
        return Response({
            'message': 'Harverst instance created successfully',
            'id': harverst_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_packaging(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for Packaging: {data}")
    serializer = PackagingSerializer(data=data)
    if serializer.is_valid():
        packaging_instance = serializer.save()
        return Response({
            'message': 'Packaging instance created successfully',
            'id': packaging_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_procurement(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for Procurement: {data}")
    serializer = ProcurementSerializer(data=data)
    if serializer.is_valid():
        procurement_instance = serializer.save()
        return Response({
            'message': 'Procurement instance created successfully',
            'id': procurement_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_packing(request):
    data = request.data.copy()
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    ic(f"Received data for Packing: {data}")
    serializer = PackingSerializer(data=data)
    if serializer.is_valid():
        packing_instance = serializer.save()
        return Response({
            'message': 'Packing instance created successfully',
            'id': packing_instance.id
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
