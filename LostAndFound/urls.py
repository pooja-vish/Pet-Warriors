# urls.py in LostAndFound
from django.urls import path
from LostAndFound import views
app_name = 'LostAndFound'

urlpatterns = [
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
    #path('lostSearch',views.lostSearch, name='lostSearch'),
    #path('foundSearch',views.foundSearch, name='foundSearch'),
]
