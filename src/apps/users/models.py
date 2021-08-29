from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

from phone_field import PhoneField


# Create your models here.
class User(AbstractUser):

    #phone_number = models.CharField(max_length=10)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    date_of_birth = models.DateField()