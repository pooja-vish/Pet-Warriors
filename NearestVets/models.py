from django.db import models

class Vet(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

class Location(models.Model):
    searchLocation = models.TextField(null=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
# Create your models here.
