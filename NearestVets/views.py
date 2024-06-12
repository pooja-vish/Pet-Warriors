from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Vet


def hello(request):
    return HttpResponse("Hello")

def nearest_vets(request):
    api_key = 'AIzaSyDHMLz7UrsQIaM6njsVykYns0NE5WcA-Sw'
    location = '42.302290,-83.053250'  # Replace with actual location
    radius = 5000  # Define the radius in meters within which to search

    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type=veterinary_care&key={api_key}"
    
    response = requests.get(url)
    results = response.json().get('results', [])
    
    vets = []
    for place in results:
        vet = {
            'name': place.get('name'),
            'address': place.get('vicinity'),
            'place_id': place.get('place_id'),
        }
        # Get more details if required using place details API
        vets.append(vet)
    
    return render(request, 'nearest_vets.html', {'vets': vets})
