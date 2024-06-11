from django.db import models
from datetime import timezone
from django.db import models
from PetForum.models import Member
# Create your models here.
class Adoption():
    image = models.ImageField(upload_to ='images/'),
    description = models.TextField(),
    location = models.TextField(),
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE),
    date_posted = models.DateTimeField(default=timezone.now),
    species = models.TextField()

