from django.db import models
from company.models import Employee
# Create your models here.

class Timecard(models.Model):
    employee =  models.ForeignKey(Employee, on_delete=models.CASCADE)
    day = models.DateField()
    clock_in = models.TimeField()
    lunch_in = models.TimeField(blank=True, null=True)
    lunch_out = models.TimeField(blank=True, null=True)
    clock_out = models.TimeField(blank=True, null=True)
    total = models.DecimalField(null=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.day} -- {self.employee.full_name} -- {self.employee.enterprise}'