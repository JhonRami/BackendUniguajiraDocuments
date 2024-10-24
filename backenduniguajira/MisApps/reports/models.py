from django.db import models
from MisApps.students.models import Students

class Reports(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "report"
        verbose_name_plural = "reports"

