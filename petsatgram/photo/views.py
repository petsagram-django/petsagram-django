from django.shortcuts import render, redirect

from petsatgram.main.models import PetPhoto
from petsatgram.photo.model_forms import CreatePhotoForm, EditPhotoForm


def show_photo_details(request, id):
    # use id to get specific element from the db
    photo_details = PetPhoto.objects.get(pk=id)

    context = {
        'photo_details': photo_details
    }
    return render(request, 'photo_details.html', context)


def like_photo(request, id):
    # view without render and context, use redirect to update the page with data
    photo = PetPhoto.objects.get(pk=id)
    photo.likes += 1
    photo.save()

    return redirect('photo_details', id)


def edit_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)

    if request.method == 'POST':
        photo_form = EditPhotoForm(request.POST, request.FILES, instance=photo)
        if photo_form.is_valid():
            photo_form.save()
            return redirect('photo_details', pk)
    else:
        photo_form = EditPhotoForm(instance=photo)

    photo_url = photo.photo
    context = {
        'photo_form': photo_form,
        'photo_url': photo_url,
    }

    return render(request, 'photo_edit.html', context)


def create_photo(request):
    if request.method == 'POST':
        photo_form = CreatePhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo_form.save()
            return redirect('dashboard')
    else:
        photo_form = CreatePhotoForm()

    context = {
        'photo_form': photo_form
    }

    return render(request, 'photo_create.html', context)


def delete_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.delete()
    return redirect('dashboard')
