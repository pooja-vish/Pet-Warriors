# forms.py
from django import forms
from .models import LostPet, FoundPet
#
# SPECIES_CHOICES = [
#     ('Dog', 'Dog'),
#     ('Cat', 'Cat'),
#     ('Bird', 'Bird'),
#     ('Fish', 'Fish'),
#     ('Hamster', 'Hamster'),
#     ('Rabbit', 'Rabbit'),
#     ('Reptile', 'Reptile'),
#     ('Ferret', 'Ferret'),
#     ('Guinea Pig', 'Guinea Pig'),
#     ('Horse', 'Horse'),
#     ('Turtle', 'Turtle'),
#     ('Parrot', 'Parrot'),
#     ('Chinchilla', 'Chinchilla'),
#     ('Hedgehog', 'Hedgehog'),
#     ('Pig', 'Pig'),
#     ('Goat', 'Goat'),
#     ('Other', 'Other'),  # Option for user-defined species
# ]
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
                       'placeholder': 'Enter Species like Cat/Dog', 'required': 'required'}),
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
        choice =[
            ('Dog','Dog')
        ]
        widgets = {
            'location': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'location', 'name': "location",
                       'placeholder': 'Enter Location', 'required': 'required'}),
            'description': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'description', 'name': "description",
                       'placeholder': 'Enter description', 'required': 'required'}),
            'species': forms.CharField(
                attrs={'class': 'form-control border-0 p-4', 'id': 'species', 'name': "species",
                       'placeholder': 'Enter Species example: Cat, Dog', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
