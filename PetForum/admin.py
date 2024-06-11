from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member, Question, Answer

# Register your models here.
admin.site.register(Member)
admin.site.register(Question)
admin.site.register(Answer)