from django.urls import path

from petsatgram.photo.views import show_photo_details, like_photo, edit_photo, create_photo, delete_photo

urlpatterns = [
    path('details/<int:id>', show_photo_details, name='photo_details'),
    path('details/like/<int:id>', like_photo, name='like_photo'),
    path('edit/<int:pk>', edit_photo, name='edit photo'),
    path('create/', create_photo, name='create photo'),
    path('delete/<int:pk>', delete_photo, name='delete photo')
]
