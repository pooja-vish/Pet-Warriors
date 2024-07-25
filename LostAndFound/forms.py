# forms.py
from django import forms
from .models import LostPet, FoundPet

class LostPetForm(forms.ModelForm):
    class Meta:
        model = LostPet
        fields = ['image', 'description', 'location', 'species', 'pet_name']
        widgets = {
            'location': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'location', 'name': "location",
                       'placeholder': 'Enter Location', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'description', 'name': "description",
                       'placeholder': 'Enter description', 'required': 'required'}),
            'species': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'species', 'name': "species",
                       'placeholder': 'Enter Species', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pet_name' : forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'location', 'name': "location",
                       'placeholder': 'Enter Location', 'required': 'required'}
            )
        }

class FoundPetForm(forms.ModelForm):
    class Meta:
        model = FoundPet
        fields = ['image', 'description', 'location', 'species']
        widgets = {
            'location': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'location', 'name': "location",
                       'placeholder': 'Enter Location', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'description', 'name': "description",
                       'placeholder': 'Enter description', 'required': 'required'}),
            'species': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'species', 'name': "species",
                       'placeholder': 'Enter Species', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
