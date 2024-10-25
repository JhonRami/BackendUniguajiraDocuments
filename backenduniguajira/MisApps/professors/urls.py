from django.urls import path
from MisApps.professors.views import professors_list, professors_detail

urlpatterns = [
    path('', professors_list),
    path('<int:pk>/', professors_detail),
]
