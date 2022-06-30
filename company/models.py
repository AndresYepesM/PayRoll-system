from django.db import models
from accounts.models import Account

# Create your models here.

class Enterprise(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zipcode = models.IntegerField()

    def __str__(self):
        return f'{self.name} ---- {self.email}'
