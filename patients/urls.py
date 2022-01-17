# patients/urls.py
from django.urls import path
from .views import (
    PatientListView,
    PatientDetailView,
    PatientUpdateView,
    PatientDeleteView,
)

urlpatterns = [
    path("<int:pk>/", PatientDetailView.as_view(),
        name="patient_detail"),  # new
    path("<int:pk>/edit/", PatientUpdateView.as_view(),
        name="patient_edit"),  # new
    path("<int:pk>/delete/", PatientDeleteView.as_view(),
        name="patient_delete"),  # new
    path("", PatientListView.as_view(), name="patient_list"), 


]