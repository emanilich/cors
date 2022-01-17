from django import forms
from django.forms import ModelForm
from .models import Patient
 
class DateInput(forms.DateInput):
    input_type = 'date'
 
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            "mrn",
            "first_name",
            'last_name',
            'dob',
        )
        widgets = {
            'dob': DateInput()
        }
        