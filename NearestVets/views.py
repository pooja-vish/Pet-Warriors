# views.py
from django.http import HttpResponse
from django.shortcuts import render
import threading
import time
from .models import Vet
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

# Global variable to hold fetched data
fetched_data = []

# Function to refresh data from Google API
def refresh_data():
    global fetched_data
    api_key =  'AIzaSyDHMLz7UrsQIaM6njsVykYns0NE5WcA-Sw'  # Replace with your actual Google API key
    location = '42.302290,-83.053250'  # Replace with actual location
    radius = 5000  # Define the radius in meters within which to search

    fetched_data = fetch_google_places(api_key, location, radius)
    print(f"[DEBUG] Data refreshed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Background thread function to run refresh every 6 hours
def background_refresh():
    while True:
        refresh_data()
        # Sleep for 6 hours (in seconds)
        time.sleep(6*60*60)

# Start the background thread when Django starts
refresh_thread = threading.Thread(target=background_refresh)
refresh_thread.daemon = True  # Daemonize the thread so it stops with the server
refresh_thread.start()

def hello(request):
    return HttpResponse("Hello")

def nearest_vets(request):
    global fetched_data
    # Use the globally fetched data
    vets = fetched_data
    
    return render(request, 'nearest_vets.html', {'vets': vets})
