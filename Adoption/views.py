from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adoption, Member
from .forms import AdoptionForm, AdoptionSearchForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def adoption_search(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST, request.FILES)
        if form.is_valid():
            newform = Adoption()
    else:
        newform = Adoption()
    posts = Adoption.objects.all().order_by('species')
    return render(request, 'Adoption/adoption.html', {'newform': newform, 'posts': posts})


def adoption(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST, request.FILES)
        searchform = AdoptionSearchForm(request.POST)
        if form.is_valid():
            #user = request.user
            form.save()
            form = AdoptionForm()
    else:
        form = AdoptionForm()
        searchForm = AdoptionSearchForm()
        species = ''
       # species = form.cleaned_data['species']
        print('species')
        if species:
            posts = Adoption.objects.filter(species=species)
        else:
            posts = Adoption.objects.all().order_by('-id')
    return render(request, 'Adoption/adoption.html', {'form': form, 'searchForm': searchForm, 'posts': posts})
