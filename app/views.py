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
from django.core.cache import cache
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
