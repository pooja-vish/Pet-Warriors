"""
URL configuration for PetWarrior project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from LoginSignup.views import CustomSignupView
from PetForum import views, urls
from Adoption import views, urls
from LoginSignup import views, urls
from NearestVets import views, urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PetForum.urls')),
    path('', include('Adoption.urls')),
    path('', include('LoginSignup.urls')),

    #path('',include('googleauthentication.urls')),
    path('accounts/', include('allauth.urls')),

    path('nearest-vets/', include('NearestVets.urls')),

]
