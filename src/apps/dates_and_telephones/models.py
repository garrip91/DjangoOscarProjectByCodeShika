from django.db import models

#from oscar.apps.customer.abstract_models import AbstractUser

#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class PhoneAndDate(models.Model):

    phone_number = models.CharField(max_length=18, unique=True, verbose_name='Номер телефона', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)