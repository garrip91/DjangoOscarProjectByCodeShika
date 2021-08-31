from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser


# Create your models here.
class User(AbstractUser):

    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()