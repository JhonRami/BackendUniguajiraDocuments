from django.urls import path
from MisApps.reports.views import reports_list, reports_detail

urlpatterns = [
    path('', reports_list),
    path('<int:pk>/', reports_detail),
]
