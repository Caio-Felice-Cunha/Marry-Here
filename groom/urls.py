from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('guests_list', views.guests_list, name='guests_list')
]