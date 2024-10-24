from django.urls import path
from MisApps.loans.views import loans_list, loans_detail

urlpatterns = [
    path('', loans_list),
    path('<int:pk>/', loans_detail),
]
