from django.urls import path
from .views import add_patient  # import only views from this app

urlpatterns = [
    path('add/', add_patient, name='add_patient'),
]