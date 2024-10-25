from django.contrib import admin
from MisApps.students.models import Students

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Students, StudentsAdmin)