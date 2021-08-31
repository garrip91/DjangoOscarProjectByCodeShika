from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    phone_number = PhoneNumberField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)


from oscar.apps.customer.models import *  # noqa isort:skip
