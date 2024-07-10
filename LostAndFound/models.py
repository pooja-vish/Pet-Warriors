# models.py
from django.db import models
from django.contrib.auth.models import User

class LostPet(models.Model):
    image = models.ImageField(upload_to='lost_pets/')
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    species = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100, blank=True, null=True)  # Optional

    def __str__(self):
        return f"Lost Pet: {self.pet_name if self.pet_name else self.species} at {self.location}"

class FoundPet(models.Model):
    image = models.ImageField(upload_to='found_pets/')
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    species = models.CharField(max_length=100)

    def __str__(self):
        return f"Found Pet: {self.species} at {self.location}"