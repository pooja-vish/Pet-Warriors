from django.urls import path
from PetForum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/', views.forum, name='forum'),
<<<<<<< HEAD
]
=======
    path('question_submit/', views.question_submit, name='question_submit'),
    path('answer_submit/', views.answer_submit, name='answer_submit'),
]
>>>>>>> 483db394b11eb08820a37dd552a81764791c90ff
