from django.urls import path

from petsatgram.profile_app.views import show_profile, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', show_profile, name='profile'),
    path('create/', create_profile, name='create profile'),
    path('edit/<int:pk>', edit_profile, name='edit profile'),
    path('delete/<int:pk>', delete_profile, name='delete profile'),
)
