from django.db import models

from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    phone_number = models.CharField(max_length=18, unique=True, verbose_name='Номер телефона', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)


from oscar.apps.customer.models import *  # noqa isort:skip
