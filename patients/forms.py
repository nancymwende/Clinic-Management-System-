from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'gender', 'phone_number']
      