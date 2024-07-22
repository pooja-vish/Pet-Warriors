from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Member(User):
    address = models.CharField(max_length=500)
    country = models.CharField(max_length=300, default='Canada')
    province = models.CharField(max_length=10, default='ON')
    city = models.CharField(max_length=500, default='Windsor')
<<<<<<< HEAD
    mobileNo = models.IntegerField()

=======
    mobileNo = PhoneNumberField()
>>>>>>> 483db394b11eb08820a37dd552a81764791c90ff

class Category(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title

class Question(models.Model):
    question_id = models.AutoField(primary_key=True, auto_created=True)
    question = models.TextField(null=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='category')
    creationDate = models.DateTimeField(default=timezone.now)
    updationDate = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    answer = models.TextField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(default=timezone.now)
    updationDate = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
