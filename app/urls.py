from django.urls import path
from . import views
from django.core.cache import cache  # New import for shared storage
from icecream import ic  # Assuming you are using icecream for debugging
from .models import *  # Import your models including LandPrep
urlpatterns = [
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('display_data/<str:data_id>/', views.display_data, name='display_data'),
    path('create_landprep/', views.create_landprep, name='create_landprep'),
]