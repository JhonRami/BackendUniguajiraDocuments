from django.db import models

class Programsdir(models.Model):
    name = models.CharField(max_length=255, help_text="Enter the director name") 
    address = models.CharField(max_length=100, help_text="Enter the director address")
    phone = models.CharField(max_length=12, help_text="Enter the director phone number")
    email = models.EmailField(max_length=100, help_text="Enter the director email")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "programsdir"
        verbose_name_plural = "programsdir"