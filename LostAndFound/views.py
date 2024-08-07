from django.shortcuts import render, redirect
from .models import LostPet, FoundPet
from .forms import LostPetForm, FoundPetForm
from django.db.models import Q
from .models import FoundPet, LostPet


def lostSearch(request):
    posts = []
    #form = AdoptionForm(request.POST or None)
    if request.method == 'POST':
        species = request.POST.get('species')
        if species:
            pets = LostPet.objects.filter(species__icontains=species)
        else:
            pets = LostPet.objects.all().order_by('-id')
    else:
        pets = LostPet.objects.all().order_by('date_posted')
    form = LostPet()
    return render(request, 'LostAndFound/lost.html', {'form': form, 'pets': pets})

def lost(request):
    if request.method == 'POST':
        form = LostPetForm(request.POST, request.FILES)
        if form.is_valid():
            lost_pet = form.save(commit=False)
            lost_pet.user = request.user  # Associate the pet with the current user
            lost_pet.save()
            form = LostPetForm()
            # return redirect('found')
    else:
        form = LostPetForm()

    search_query = request.GET.get('q', '')
    if search_query:
        pets = LostPet.objects.filter(
                Q(species__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(location__icontains=search_query)
            )
    else:
        pets = LostPet.objects.all()
    context = {
        'form': form,
        'pets': pets,
        'searchForm': form  # Assuming form is used for search; adjust if separate search form is used

        }
    return render(request, 'LostAndFound/lost.html', context)

def found(request):
    if request.method == 'POST':
        form = FoundPetForm(request.POST, request.FILES)
        if form.is_valid():
            found_pet = form.save(commit=False)
            found_pet.user = request.user  # Associate the pet with the current user
            found_pet.save()
            form = FoundPetForm()
            # return redirect('found')
    else:
        form = FoundPetForm()

    search_query = request.GET.get('q', '')
    if search_query:
        pets = FoundPet.objects.filter(
            Q(species__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    else:
        pets = FoundPet.objects.all()
    # posts = Adoption.objects.all().order_by('-id')
    context = {
        'form': form,
        'pets': pets,
        'searchForm': form  # Assuming form is used for search; adjust if separate search form is used
    }
    return render(request, 'LostAndFound/found.html', context)
def foundSearch(request):
    posts = []
    #form = AdoptionForm(request.POST or None)
    if request.method == 'POST':
        species = request.POST.get('species')
        if species:
            pets = FoundPet.objects.filter(species__icontains=species)
        else:
            pets = FoundPet.objects.all().order_by('-id')
    else:
        pets = FoundPet.objects.all().order_by('date_posted')
    form = FoundPet()
    return render(request, 'LostAndFound/found.html', {'form': form, 'pets': pets})
