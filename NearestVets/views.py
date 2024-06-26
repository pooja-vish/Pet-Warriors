from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Vet
import requests

def hello(request):
    return HttpResponse("Hello")

from django.shortcuts import render
import requests

# Function to fetch data from Google API
def fetch_google_places(api_key, location, radius):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'type': 'veterinary_care',
        'key': api_key,
    }
    
    response = requests.get(url, params=params)
    results = response.json().get('results', [])
    
    vets = []
    for place in results:
        vet = {
            'name': place.get('name'),
            'address': place.get('vicinity'),
            'place_id': place.get('place_id'),
        }
        # Optionally, you can fetch more details using place details API here if needed
        vets.append(vet)
    
    return vets

def nearest_vets(request):
    api_key = 'AIzaSyDHMLz7UrsQIaM6njsVykYns0NE5WcA-Sw'  # Replace with your actual Google API key
    location = '42.302290,-83.053250'  # Replace with actual latitude,longitude
    radius = 5000  # Define the radius in meters within which to search

    # Fetch data from Google API using fetch_google_places function
    vets = fetch_google_places(api_key, location, radius)
    
    return render(request, 'nearest_vets.html', {'vets': vets})
