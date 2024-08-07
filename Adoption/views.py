from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Adoption, Member
from .forms import AdoptionForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def adoptionSearch(request):
    posts = []
    if request.method == 'POST':
        species = request.POST.get('species')
        print('species=',species)
        if species:
            posts = Adoption.objects.filter(
                Q(species__icontains=species) |
                Q(description__icontains=species) |
                Q(location__icontains=species) |
                Q(other_species__icontains=species)
         )
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
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            species = form.cleaned_data['species']
            if species == 'Other':
                other_species = form.cleaned_data['other_species']
            else:
                other_species = ''
            member = Member.objects.get(username=request.user)
            adoption_object = Adoption(image=image, description=description, location=location, species=species,other_species=other_species, user_id=member)
            adoption_object.save()
            form = AdoptionForm()
    else:
        form = AdoptionForm()
    posts = Adoption.objects.all().order_by('-id')
    return render(request, 'Adoption/adoption.html', {'form': form, 'posts': posts})
