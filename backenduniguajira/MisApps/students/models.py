from django.db import models
from MisApps.programs.models import Programs 

class Students(models.Model):
    name = models.CharField(max_length=255) 
    address = models.CharField(max_length=100, help_text="Enter the student's address")
    phone = models.CharField(max_length=12, help_text="Enter the student's phone number")
    email = models.EmailField(max_length=100, help_text="Enter the student's email")
    program = models.ForeignKey(Programs, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"