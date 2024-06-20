from django.urls import path
from LoginSignup import views

urlpatterns = [
    #path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]