from django.conf import settings
from django.db import models
from django.urls import reverse

class Patient(models.Model):
    mrn = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    updated = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.mrn
    
    def get_absolute_url(self):
        return reverse("patient_detail",kwargs={"pk": self.pk})



