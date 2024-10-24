from django.contrib import admin
from MisApps.programs.models import Programs

# Register your models here.

class ProgramsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Programs, ProgramsAdmin)