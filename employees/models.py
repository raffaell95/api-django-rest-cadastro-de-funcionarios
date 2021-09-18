from django.db import models
from departments.models import Department

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
