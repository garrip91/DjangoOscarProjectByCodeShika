from django import forms
from .models import PhoneAndDate
#from phonenumber_field.formfields import PhoneNumberField
#from phonenumber_field.widgets import PhoneNumberPrefixWidget


class PhoneAndDateForm(forms.ModelForm):

    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))
    
    class Meta:
        model = PhoneAndDate
        fields = ['phone_number']