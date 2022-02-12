from django.shortcuts import render, redirect

from petsatgram.main.models import Pet
from petsatgram.pet.model_forms import PetCreateForm


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet_form = PetCreateForm(request.POST, instance=pet)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('profile')
    else:
        pet_form = PetCreateForm(instance=pet)
        context = {
             'pet_form': pet_form
        }

        return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile')
    else:
        return render(request, 'pet_delete.html')


def create_pet(request):
    if request.method == 'POST':
        pet_form = PetCreateForm(request.POST)
        if pet_form.is_valid():
            pet_form.save()
            return redirect('profile')

    else:
        pet_form = PetCreateForm()

    context = {'pet_form': pet_form}

    return render(request, 'pet_create.html', context)
