from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_landprep/', views.create_landprep, name='create_landprep'),
    path('create_transplanting/', views.create_transplanting, name='create_transplanting'),
    path('create_fertilizer/', views.create_fertilizer, name='create_fertilizer'),
    path('create_harverst/', views.create_harverst, name='create_harverst'),
    path('create_packaging/', views.create_packaging, name='create_packaging'),
    path('create_procurement/', views.create_procurement, name='create_procurement'),
    path('create_packing/', views.create_packing, name='create_packing'),
    path('clear_all_data/', views.clear_all_data, name='clear_all_data'),
    path('get_data/', views.display_data, name='get_data'),
    path('display_data_html/', views.display_data, name='display_data_html'),

    path('get_landprep/', views.get_landprep, name='get_landprep'),
    path('get_transplanting/', views.get_transplanting, name='get_transplanting'),
    path('get_fertilizer/', views.get_fertilizer, name='get_fertilizer'),
    path('get_harverst/', views.get_harverst, name='get_harverst'),
    path('get_packaging/', views.get_packaging, name='get_packaging'),
    path('get_procurement/', views.get_procurement, name='get_procurement'),
    path('get_packing/', views.get_packing, name='get_packing'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
