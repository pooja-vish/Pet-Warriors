from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adoption, Member
from .forms import AdoptionForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def adoptionSearch(request):
    posts = []
    #form = AdoptionForm(request.POST or None)
    if request.method == 'POST':
        species = request.POST.get('species')
        if species:
            posts = Adoption.objects.filter(species__icontains=species)
        else:
            posts = Adoption.objects.all().order_by('-id')
    else:
        posts = Adoption.objects.all().order_by('date_posted')
    form = AdoptionForm()
    return render(request, 'Adoption/adoption.html', {'form': form, 'posts': posts})


def adoption(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            #user = request.user
            form.save()
            form = AdoptionForm()
    else:
        form = AdoptionForm()
    posts = Adoption.objects.all().order_by('-id')
    return render(request, 'Adoption/adoption.html', {'form': form,  'posts': posts})
