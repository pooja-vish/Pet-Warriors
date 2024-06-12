from django.db import models

class Vet(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
# Create your models here.
