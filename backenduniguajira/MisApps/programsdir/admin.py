from django.contrib import admin
from MisApps.programsdir.models import Programsdir

# Register your models here.

class ProgramsdirAdmin(admin.ModelAdmin):
    pass


admin.site.register(Programsdir, ProgramsdirAdmin)