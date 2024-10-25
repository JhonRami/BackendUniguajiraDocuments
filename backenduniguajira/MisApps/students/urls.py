from django.urls import path
from MisApps.students.views import students_list, students_detail

urlpatterns = [
    path('', students_list),
    path('<int:pk>/', students_detail),
]
