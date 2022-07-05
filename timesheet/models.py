from django.db import models
from company.models import Employee
# Create your models here.

class Timecard(models.Model):
    employeee =  models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=True)
    clock_in = models.DateTimeField(blank=True)
    lunch_in = models.DateTimeField(blank=True)
    lunch_out = models.DateTimeField(blank=True)
    clock_out = models.DateTimeField(blank=True)
    total = models.IntegerField()

    def __str__(self):
        return f'{self.day}'