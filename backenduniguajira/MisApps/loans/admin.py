from django.contrib import admin
from MisApps.loans.models import Loans

# Register your models here.

class LoansAdmin(admin.ModelAdmin):
    pass


admin.site.register(Loans, LoansAdmin)
