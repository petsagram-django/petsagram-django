from django.urls import path

from petsatgram.pet.views import create_pet, edit_pet, delete_pet

urlpatterns = [
    path('create/', create_pet, name='create pet'),
    path('edit/<int:pk>', edit_pet, name='edit pet'),
    path('delete/<int:pk>', delete_pet, name='delete pet')
]
