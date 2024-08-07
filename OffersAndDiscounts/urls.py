# OffersAndDiscounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.offers_view, name='offers'),
    path('offers_view', views.offers_view, name='offers_view'),
]
