from django.urls import path
from PetForum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/', views.forum, name='forum'),



    path('question_submit/', views.question_submit, name='question_submit'),
    path('answer_submit/', views.answer_submit, name='answer_submit'),
]

