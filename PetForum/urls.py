from django.urls import path
from PetForum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/', views.forum, name='forum'),
]