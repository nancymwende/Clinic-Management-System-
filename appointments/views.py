from .forms import AppointmentForm
from django.shortcuts import render, redirect

def book_appointment(request):
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'book_appointment.html', {'form': form})