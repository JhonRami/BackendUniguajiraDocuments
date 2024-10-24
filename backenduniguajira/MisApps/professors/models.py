from django.db import models
from MisApps.programs.models import Programs

class Professors(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100, help_text="Enter the professor address")
    phone = models.CharField(max_length=12, help_text="Enter the director professor number")
    email = models.EmailField(max_length=100, help_text="Enter the proffesor email")
    program = models.ForeignKey(Programs, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "professor"
        verbose_name_plural = "professors"