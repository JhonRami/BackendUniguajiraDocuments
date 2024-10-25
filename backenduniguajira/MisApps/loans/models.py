from django.db import models
from MisApps.students.models import Students

class Loans(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    namebook = models.CharField(max_length=255)
    dateloans = models.DateField()
    datereturn = models.DateField()

    def __str__(self):
        return self.namebook

    class Meta:
        verbose_name = "loan"
        verbose_name_plural = "loans"