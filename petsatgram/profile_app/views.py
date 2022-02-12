from django.shortcuts import render, redirect

from petsatgram.main.models import Profile
from petsatgram.main.views import get_first_profile
from petsatgram.profile_app.model_forms import ProfileCreateForm, ProfileEditForm


def show_profile(request):
    profile = get_first_profile()
    photos = profile.petphoto_set.all()
    likes = sum([photo.likes for photo in photos])
    pets = profile.pet_set.all()

    context = {
        'profile': profile,
        'likes': likes,
        'pets': pets,
    }
    return render(request, 'profile_details.html', context)


def create_profile(request):
    if request.method == 'POST':

        profile_form = ProfileCreateForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')

    else:
        profile_form = ProfileCreateForm()

    context = {'profile_form': profile_form}

    return render(request, 'profile_create.html', context)


def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')

    else:
        profile_form = ProfileEditForm(
            instance=profile,
        )

    context = {'profile_form': profile_form}

    return render(request, 'profile_edit.html', context)


def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':
        profile.delete()

        return redirect('index')
    else:
        return render(request, 'profile_delete.html')
