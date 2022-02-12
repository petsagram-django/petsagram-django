from django.shortcuts import render, redirect

from petsatgram.main.models import Profile, PetPhoto


def get_first_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    # add context if you want to give data to the template
    context = {
        'home_view': True
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_first_profile()
    # property_set.all() to get one to many relations
    pets_photos = profile.petphoto_set.all()
    print(pets_photos)
    context = {
        'pet_photos': pets_photos
    }

    return render(request, 'dashboard.html', context)





def show404(request, exception):
    return render(request, '404_error.html')

