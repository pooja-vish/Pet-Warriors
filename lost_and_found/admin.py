from django.contrib import admin
from .models import FoundPet, LostPet

@admin.register(FoundPet)
class FoundPetAdmin(admin.ModelAdmin):
    list_display = ('species', 'location', 'date_posted', 'user')
    search_fields = ('species', 'location')
    list_filter = ('date_posted',)

@admin.register(LostPet)
class LostPetAdmin(admin.ModelAdmin):
    list_display = ('species', 'location', 'date_posted', 'user', 'pet_name')
    search_fields = ('species', 'location', 'pet_name')
    list_filter = ('date_posted',)
