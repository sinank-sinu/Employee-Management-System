# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
       return self.name
   