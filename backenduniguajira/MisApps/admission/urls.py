from django.urls import path
from MisApps.admission.views import admission_list, admission_detail

urlpatterns = [
    path('', admission_list),
    path('<int:pk>/', admission_detail),
]
