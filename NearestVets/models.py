from django.db import models

class Vet(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

class location(models.Model):
    searchLocation = models.TextField(null=False)
# Create your models here.
