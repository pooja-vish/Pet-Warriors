from django.shortcuts import render, redirect
from .models import LostPet, FoundPet
from .forms import LostPetForm, FoundPetForm
from django.db.models import Q
from .models import FoundPet, LostPet

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
