from django.shortcuts import render
from .forms import PatientForm


def home(request):
    return render(request, 'home.html')

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})