from django.urls import path
from . import views

urlpatterns = [
    path('', views.guests, name='guests'),
    path('answer_attendance/', views.answer_attendance, name='answer_attendance'),
    path('reserve_gift/<int:id>', views.reserve_gift, name='reserve_gift')
]