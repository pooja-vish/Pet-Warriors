# forms.py
from django import forms
from .models import LostPet, FoundPet


class LostPetForm(forms.ModelForm):
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Fish', 'Fish'),
        ('Hamster', 'Hamster'),
        ('Rabbit', 'Rabbit'),
        ('Reptile', 'Reptile'),
        ('Ferret', 'Ferret'),
        ('Guinea Pig', 'Guinea Pig'),
        ('Horse', 'Horse'),
        ('Turtle', 'Turtle'),
        ('Parrot', 'Parrot'),
        ('Chinchilla', 'Chinchilla'),
        ('Hedgehog', 'Hedgehog'),
        ('Pig', 'Pig'),
        ('Goat', 'Goat'),
        ('Other', 'Other'),
    ]

    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        initial='Dog',
        widget=forms.Select(attrs={
            'class': 'form-control border-0 p-4',
            'id': 'species',
            'name': 'species',
            'required': 'required',
            'placeholder': 'Enter species'
        })
    )
    other_species = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 p-4',
            'id': 'other_species',
            'name': 'other_species',
            'placeholder': 'Enter species if other',
        }),
        label=''
    )

    class Meta:
        model = LostPet
        fields = ['image', 'description', 'location', 'species', 'pet_name','other_species']
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
            'pet_name': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'id': 'location', 'name': "location",
                       'placeholder': 'Enter Location', 'required': 'required'}
            )
        }


class FoundPetForm(forms.ModelForm):
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Fish', 'Fish'),
        ('Hamster', 'Hamster'),
        ('Rabbit', 'Rabbit'),
        ('Reptile', 'Reptile'),
        ('Ferret', 'Ferret'),
        ('Guinea Pig', 'Guinea Pig'),
        ('Horse', 'Horse'),
        ('Turtle', 'Turtle'),
        ('Parrot', 'Parrot'),
        ('Chinchilla', 'Chinchilla'),
        ('Hedgehog', 'Hedgehog'),
        ('Pig', 'Pig'),
        ('Goat', 'Goat'),
        ('Other', 'Other'),
    ]

    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        initial='Dog',
        widget=forms.Select(attrs={
            'class': 'form-control border-0 p-4',
            'id': 'species',
            'name': 'species',
            'required': 'required',
            'placeholder': 'Enter species'
        })
    )
    other_species = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-0 p-4',
            'id': 'other_species',
            'name': 'other_species',
            'placeholder': 'Enter species if other',
        }),
        label=''
    )
    class Meta:
        model = FoundPet
        fields = ['image', 'description', 'location', 'species','other_species']
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

