from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=1)
    
    