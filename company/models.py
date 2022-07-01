from django.db import models
from accounts.models import Account

# Create your models here.

class Enterprise(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
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

class Position(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35)
    ssn = models.IntegerField(unique=True)
    salary = models.FloatField()
    role = models.OneToOneField(Position, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} name: {self.full_name},  company id: {self.enterprise.id}'
