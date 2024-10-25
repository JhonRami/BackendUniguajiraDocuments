from django.db import models
from MisApps.students.models import Students

class Admission(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    dateadmission = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dateadmission} - {self.status}"
    
    class Meta:
        verbose_name = "admission"
        verbose_name_plural = "admissions"

