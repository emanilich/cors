from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView 
from django.urls import reverse_lazy
from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


from .models import Patient
from .forms import PatientForm

class PatientListView(LoginRequiredMixin, ListView): 
    model = Patient
    template_name = "patient_list.html"

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patient_detail.html"

class DateInput(forms.DateInput):
    input_type = 'date'

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "patient_edit.html"
    def get_success_url(self):
        return reverse_lazy('patient_edit', args=[self.object.pk])
    
class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "patient_delete.html"
    success_url = reverse_lazy("patient_list")
