import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from icecream import ic
from .models import *
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
    # if a file is provided in request.FILES, prefer it over base64 data
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

@api_view(['POST'])
def clear_all_data(request):
    # List all models and their photo fields
    model_photo_fields = [
        (landprep, 'photo'),
        (transplanting, 'photo'),
        (fertilizer, 'photo'),
        (harverst, 'photo'),
        (packaging, 'photo'),
        (Procurement, 'photo'),
        (packing, 'photo'),
    ]
    # Delete all media files for each model
    for model, photo_field in model_photo_fields:
        for obj in model.objects.all():
            photo = getattr(obj, photo_field, None)
            if photo and hasattr(photo, 'path') and os.path.isfile(photo.path):
                try:
                    os.remove(photo.path)
                except Exception:
                    pass
    # Delete all records from each model
    for model, _ in model_photo_fields:
        model.objects.all().delete()
    return Response({'message': 'All data and media files have been deleted.'}, status=status.HTTP_200_OK)