from django.urls import path
from .views import doctors_list

urlpatterns = [
    path('list/', doctors_list, name='doctors_list'),
]