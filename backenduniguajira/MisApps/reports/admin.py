from django.contrib import admin
from MisApps.reports.models import Reports

# Register your models here.

class ReportsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Reports, ReportsAdmin)