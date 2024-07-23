from django.db import models
from django.utils import timezone
from django.db import models
from PetForum.models import Member
# Create your models here.
class Adoption(models.Model):
    image = models.ImageField(upload_to ='img/', default='img/image1.jpg')
    description = models.TextField()
    location = models.TextField()
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    species = models.TextField()

