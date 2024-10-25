from django.contrib import admin
from MisApps.professors.models import Professors

# Register your models here.

class ProfessorsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Professors, ProfessorsAdmin)