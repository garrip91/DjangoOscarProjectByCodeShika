from django import forms
from .models import User
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(forms.ModelForm):

    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='IN')
    )
    #phone_number = PhoneNumberField(label="Phone", widget = PhoneNumberPrefixWidget)
    
    class Meta:
        model = User
        fields = ['phone_number', 'date_of_birth']