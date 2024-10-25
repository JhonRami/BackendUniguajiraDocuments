from django.contrib import admin
from MisApps.admission.models import Admission

# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Admission, AdmissionAdmin)
