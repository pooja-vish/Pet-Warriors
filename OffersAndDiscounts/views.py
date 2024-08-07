# OffersAndDiscounts/views.py
from django.shortcuts import render
from .models import Offer
import os
from django.conf import settings
def offers_view(request):
    file_path = None
    if request.method == 'POST':
        selected_value = request.POST.get('animals')
        print(selected_value)
        if selected_value == "dog" or selected_value == "":
            file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Dog deals.txt')
        elif selected_value == "cat":
            file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Cat deals.txt')
        elif selected_value == "bird":
            file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Bird deals.txt')
        elif selected_value == "fish":
            file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Fish deals.txt')
        elif selected_value == "reptile":
            file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Reptile deals.txt')
        elif selected_value == "small_pets":
            file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Small pet deals.txt')
    else:
        file_path = os.path.join(settings.BASE_DIR, 'scraped_files', 'Dog deals.txt')
    deals = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 5):
                if i + 5 < len(lines):
                    deal = {

                        'description': lines[i].strip(),
                        'url': lines[i + 1].strip(),
                        'old_price_label': lines[i + 3].strip(),
                    }
                    deals.append(deal)
    except FileNotFoundError:
        deals = [{"description": "File not found."}]

    context = {
        'deals': deals
    }
    return render(request, 'OffersAndDiscounts/offers.html', context)
