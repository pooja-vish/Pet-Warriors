# OffersAndDiscounts/views.py
from django.shortcuts import render
from .models import Offer

def offers_view(request):
   # offers = Offer.objects.all()
    return render(request, 'OffersAndDiscounts/offers.html')
