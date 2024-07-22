from django import forms
from django.contrib.auth.forms import UserCreationForm
from PetForum.models import Member
from phonenumber_field.formfields import PhoneNumberField

class MemberRegistrationForm(UserCreationForm):
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput()  # No 'attrs' here
    )
    country = forms.CharField(
        label='Country',
        initial='Canada',
        widget=forms.TextInput()  # No 'attrs' here
    )
    province = forms.ChoiceField(
        choices=[('ON', 'Ontario'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'),
                 ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NS', 'Nova Scotia'),
                 ('NT', 'Northwest Territories'), ('NU', 'Nunavut'), ('PE', 'Prince Edward Island'),
                 ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon')],
        initial='ON',
        widget=forms.Select()  # No 'attrs' here
    )
    city = forms.CharField(
        label='City',
        initial='Windsor',
        widget=forms.TextInput()  # No 'attrs' here
    )
    mobileNo = PhoneNumberField(
        label='Mobile Number',
        widget=forms.TextInput()  # No 'attrs' here
    )

    class Meta:
        model = Member
        fields = ['username', 'address', 'country', 'province', 'city', 'mobileNo', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return password2
