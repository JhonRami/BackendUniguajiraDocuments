from django.urls import path
from MisApps.programs.views import programs_list, programs_detail

urlpatterns = [
    path('', programs_list),
    path('<int:pk>/', programs_detail),
]
