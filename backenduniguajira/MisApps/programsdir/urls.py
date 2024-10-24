from django.urls import path
from MisApps.programsdir.views import programsdir_list, programsdir_detail

urlpatterns = [
    path('', programsdir_list),
    path('<int:pk>/', programsdir_detail),
]
