from django import forms
from .models import LostPet, FoundPet

# Define the species choices
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
    ('Other', 'Other'),  # Option for user-defined species
]


class LostPetForm(forms.ModelForm):
    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control border-0 p-4', 'id': 'id_species', 'required': 'required'})
    )
    other_species = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-0 p-4', 'id': 'id_other_species',
                   'placeholder': 'Specify other species'}),
        label='If Other, please specify'
    )

    class Meta:
        model = LostPet
        fields = ['image', 'description', 'location', 'species', 'other_species', 'pet_name']
        widgets = {
            'location': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Enter Location', 'required': 'required'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Enter description', 'required': 'required'}
            ),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pet_name': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Enter Pet Name', 'required': 'required'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(LostPetForm, self).__init__(*args, **kwargs)
        # Set the initial visibility of the other_species field based on initial data
        if self.initial.get('species') == 'Other':
            self.fields['other_species'].widget.attrs['style'] = 'display: block;'
        else:
            self.fields['other_species'].widget.attrs['style'] = 'display: block;'

    def clean(self):
        cleaned_data = super().clean()
        species = cleaned_data.get('species')
        other_species = cleaned_data.get('other_species')

        if species == 'Other' and not other_species:
            self.add_error('other_species', 'Please specify the species.')
        elif species != 'Other' and other_species:
            self.add_error('other_species', 'Please leave the "Other species" field blank.')


class FoundPetForm(forms.ModelForm):
    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-control border-0 p-4', 'id': 'id_species', 'required': 'required'})
    )
    other_species = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control border-0 p-4', 'id': 'id_other_species',
                   'placeholder': 'Specify other species'}),
        label='If Other, please specify'
    )

    class Meta:
        model = FoundPet
        fields = ['image', 'description', 'location', 'species', 'other_species']
        widgets = {
            'location': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Enter Location', 'required': 'required'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'form-control border-0 p-4', 'placeholder': 'Enter description', 'required': 'required'}
            ),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super(FoundPetForm, self).__init__(*args, **kwargs)
        # Set the initial visibility of the other_species field based on initial data
        if self.initial.get('species') == 'Other':
            self.fields['other_species'].widget.attrs['style'] = 'display: block;'
        else:
            self.fields['other_species'].widget.attrs['style'] = 'display: block;'
