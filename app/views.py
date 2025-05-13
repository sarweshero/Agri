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
    if 'photo' in request.FILES:
        data['photo'] = request.FILES['photo']
    param_id = request.query_params.get('id') or request.GET.get('id')
    if param_id:
        data['belongs_to'] = param_id
    #ic(f"Received data for LandPrep: {data}")
    instance = landprep.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = LandPrepSerializer(instance, data=data, partial=True)
    else:
        serializer = LandPrepSerializer(data=data)
    if serializer.is_valid():
        landprep_instance = serializer.save()
        return Response({
            'message': 'LandPrep instance created/updated successfully',
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
    #ic(f"Received data for Transplanting: {data}")
    instance = transplanting.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = TransplantingSerializer(instance, data=data, partial=True)
    else:
        serializer = TransplantingSerializer(data=data)
    if serializer.is_valid():
        transplanting_instance = serializer.save()
        return Response({
            'message': 'Transplanting instance created/updated successfully',
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
    #ic(f"Received data for Fertilizer: {data}")
    instance = fertilizer.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = FertilizerSerializer(instance, data=data, partial=True)
    else:
        serializer = FertilizerSerializer(data=data)
    if serializer.is_valid():
        fertilizer_instance = serializer.save()
        return Response({
            'message': 'Fertilizer instance created/updated successfully',
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
    #ic(f"Received data for Harverst: {data}")
    instance = harverst.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = HarverstSerializer(instance, data=data, partial=True)
    else:
        serializer = HarverstSerializer(data=data)
    if serializer.is_valid():
        harverst_instance = serializer.save()
        return Response({
            'message': 'Harverst instance created/updated successfully',
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
    #ic(f"Received data for Packaging: {data}")
    instance = packaging.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = PackagingSerializer(instance, data=data, partial=True)
    else:
        serializer = PackagingSerializer(data=data)
    if serializer.is_valid():
        packaging_instance = serializer.save()
        return Response({
            'message': 'Packaging instance created/updated successfully',
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
    #ic(f"Received data for Procurement: {data}")
    instance = Procurement.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = ProcurementSerializer(instance, data=data, partial=True)
    else:
        serializer = ProcurementSerializer(data=data)
    if serializer.is_valid():
        procurement_instance = serializer.save()
        return Response({
            'message': 'Procurement instance created/updated successfully',
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
    # ic(f"Received data for Packing: {data}")
    instance = packing.objects.filter(belongs_to=param_id).first()
    if instance:
        serializer = PackingSerializer(instance, data=data, partial=True)
    else:
        serializer = PackingSerializer(data=data)
    if serializer.is_valid():
        packing_instance = serializer.save()
        return Response({
            'message': 'Packing instance created/updated successfully',
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

@api_view(['GET'])
def display_data(request):
    param_id = request.query_params.get('id') or request.GET.get('id')
    if not param_id:
        return Response({'error': 'ID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        landprep_instance = landprep.objects.filter(belongs_to=param_id).order_by('-id').first()
        transplanting_instance = transplanting.objects.filter(belongs_to=param_id).order_by('-id').first()
        fertilizer_instance = fertilizer.objects.filter(belongs_to=param_id).order_by('-id').first()
        harverst_instance = harverst.objects.filter(belongs_to=param_id).order_by('-id').first()
        packaging_instance = packaging.objects.filter(belongs_to=param_id).order_by('-id').first()
        procurement_instance = Procurement.objects.filter(belongs_to=param_id).order_by('-id').first()
        packing_instance = packing.objects.filter(belongs_to=param_id).order_by('-id').first()

        data = {
            'landprep': LandPrepSerializer(landprep_instance).data if landprep_instance else None,
            'transplanting': TransplantingSerializer(transplanting_instance).data if transplanting_instance else None,
            'fertilizer': FertilizerSerializer(fertilizer_instance).data if fertilizer_instance else None,
            'harverst': HarverstSerializer(harverst_instance).data if harverst_instance else None,
            'packaging': PackagingSerializer(packaging_instance).data if packaging_instance else None,
            'procurement': ProcurementSerializer(procurement_instance).data if procurement_instance else None,
            'packing': PackingSerializer(packing_instance).data if packing_instance else None,
        }
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': f'An error occurred: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)