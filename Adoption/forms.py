from django import forms
from .models import Adoption


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['image', 'description', 'location', 'species', 'user_id']
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

