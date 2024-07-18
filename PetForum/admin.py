from django.contrib import admin
from .models import Member, Category, Question, Answer

# Register your models here.
admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Question)