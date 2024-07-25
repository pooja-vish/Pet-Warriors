from django.urls import path
from Adoption import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adoption/', views.adoption, name='adoption'),
    path('adoptionSearch/', views.adoptionSearch, name='adoptionSearch')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)