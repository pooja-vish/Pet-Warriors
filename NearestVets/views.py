from django.http import HttpResponse
from django.shortcuts import render
import threading
import time
import requests
from django.shortcuts import redirect

from NearestVets.models import Location


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
            'photo_url': get_photo_url(place, api_key)  # Fetch photo URL or Street View if no regular photos
        }
        vets.append(vet)
    
    return vets

# Function to get photo URL or street view from place details
def get_photo_url(place, api_key):
    photos = place.get('photos', [])
    if photos:
        photo_reference = photos[0].get('photo_reference', '')
        if photo_reference:
            return f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={api_key}'
    
    # If no regular photos, attempt to fetch Street View
    if place.get('geometry', {}).get('location'):
        lat = place['geometry']['location']['lat']
        lng = place['geometry']['location']['lng']
        return f'https://maps.googleapis.com/maps/api/streetview?size=400x300&location={lat},{lng}&key={api_key}'
    
    return None

# Global variable to hold fetched data
fetched_data = []

def refresh_data(location='42.302290,-83.053250', radius=5000):
    global fetched_data
    api_key = 'AIzaSyDHMLz7UrsQIaM6njsVykYns0NE5WcA-Sw'  # Constant API key
    
    # Fetch data from Google Places API
    fetched_data = fetch_google_places(api_key, location, radius)
    print(f"[DEBUG] Data refreshed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")

def refresh_data_new(request):
    if request.method == 'POST':
        location = request.POST.get('searchLocation')  # Get the selected location from POST data
        print(location, "this is me")
        radius = 5000  # Default radius value
        
        # Fetch data from Google Places API
        global fetched_data
        fetched_data = fetch_google_places(api_key='AIzaSyDHMLz7UrsQIaM6njsVykYns0NE5WcA-Sw', location=location, radius=radius)
        print(f"[DEBUG] Data refreshed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return redirect('nearest_vets')
        # Optionally, handle the fetched data or redirect to another view
        
    else:
        # Handle GET request or render the form
        locations = Location.objects.all()  # Fetch locations to populate the dropdown
        return render(request, 'NearestVets/nearest_vets.html', {'locations': locations})
    
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
    locations = Location.objects.all()
    vets = fetched_data
    return render(request, 'nearest_vets.html', {'vets': vets, 'locations': locations})