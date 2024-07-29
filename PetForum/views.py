from django.shortcuts import render, redirect
from django.contrib import admin
from .models import Member, Category, Question, Answer
from django.http import HttpResponse
from PetForum.forms import QuestionForm

# Create your views here.

def index(request):
    return render(request, 'PetForum/home.html')

def answer_submit(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        member = Member.objects.get(username=request.user)
        question = Question.objects.get(pk=request.POST['question_id'])
        answer_object = Answer.objects.create(member=member, question=question, answer=answer)
        answer_object.save()
        return redirect('forum')
    return render(request, 'PetForum/forum.html')

def question_submit(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        form.is_valid()
        question = form.cleaned_data['question']
        member = Member.objects.get(username=request.user)
        question_object = Question(question=question, member=member)
        question_object.save()
        category_ids = request.POST.getlist('category')
        question_object.category.set(category_ids)
        return redirect('forum')
    else:
        form = QuestionForm()
    return render(request, 'PetForum/forum.html', {'form': form})

def forum(request):
    form = QuestionForm()
    categories = Category.objects.all()
    posts = []
    if request.method == 'POST':
        selected_categories = request.POST.getlist('categories')
        keyword = request.POST.get('keyword')
        if keyword:
            posts = Question.objects.filter(question__icontains=keyword)
        elif selected_categories:
            for category in selected_categories:
                category_object = Category.objects.get(title=category)
                posts.extend(Question.objects.filter(category=category_object))
        else:
            posts = Question.objects.all()

    else :
        posts = Question.objects.all()
    question_with_answers = []
    for question in posts:
        answers = Answer.objects.filter(question=question)
        question_with_answers.append({'question': question, 'answers': answers, 'category': question.category.get().title})
    category_title = []
    for category in categories:
        count = Question.objects.filter(category=category).count()
        category_title.append({'category_title': category.title, 'count': count})
    members = Member.objects.all()
    return render(request, 'PetForum/forum.html', {'categories': category_title, 'posts': question_with_answers, 'members': members, 'form': form})
