from django.db import models
from MisApps.programsdir.models import Programsdir

class Programs(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey(Programsdir, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "program"
        verbose_name_plural = "programs"