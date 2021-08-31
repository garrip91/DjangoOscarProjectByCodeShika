from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

#from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):

    phone_number = PhoneNumberField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)