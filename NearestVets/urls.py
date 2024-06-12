from django.urls import path
from . import views

urlpatterns = [
   # path('', views.nearest_vets, name='nearest_vets'),
   path('', views.nearest_vets, name='nearest_vets'),
    # Add other URLs as needed
]