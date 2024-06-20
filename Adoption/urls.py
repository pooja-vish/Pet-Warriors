from django.urls import path
from Adoption import views

urlpatterns = [
    path('adoption/', views.adoption, name='adoption')
]