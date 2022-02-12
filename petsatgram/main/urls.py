from django.urls import path

from petsatgram.main.views import show_home, show_dashboard

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
)
