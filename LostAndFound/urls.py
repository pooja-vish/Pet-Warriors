# urls.py in LostAndFound
from django.urls import path
from LostAndFound import views

app_name = 'LostAndFound'

urlpatterns = [
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
    path('lostsearch/', views.lostPetSearch, name='lostPetSearch'),
    path('foundsearch/', views.foundPetSearch, name='foundPetSearch'),
]
