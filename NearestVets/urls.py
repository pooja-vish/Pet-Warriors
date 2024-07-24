from django.urls import path
from . import views

urlpatterns = [
   # path('', views.nearest_vets, name='nearest_vets'),
   path('', views.nearest_vets, name='nearest_vets'),
   path('refresh_data_new/',views.refresh_data_new, name='refresh_data_new'),
    # Add other URLs as needed
]