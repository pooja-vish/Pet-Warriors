# OffersAndDiscounts/views.py
from django.shortcuts import render
from .models import Offer

def offers_view(request):
    file_path = 'C:\\Users\\Gurekam\\Desktop\\University of Windsor\\Internship Project\\Pet-Warriors\\OffersAndDiscounts\\templates\\OffersAndDiscounts\\Files\\Dog deals.txt'
    deals = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 6):
                if i + 5 < len(lines):
                    deal = {
                        'description': lines[i].strip(),
                        'url': lines[i + 1].strip(),
                        'discounted_price_label': lines[i + 2].strip(),
                        'discounted_price': lines[i + 3].strip(),
                        'old_price_label': lines[i + 4].strip(),
                        'old_price': lines[i + 5].strip()
                    }
                    deals.append(deal)
    except FileNotFoundError:
        deals = [{"description": "File not found."}]

    context = {
        'deals': deals
    }
    return render(request, 'OffersAndDiscounts/offers.html', context)
