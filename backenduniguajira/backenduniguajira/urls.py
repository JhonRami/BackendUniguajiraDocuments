from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admission/', include('MisApps.admission.urls')),
    path('loans/', include('MisApps.loans.urls')),
    path('professors/', include('MisApps.professors.urls')),
    path('programs/', include('MisApps.programs.urls')),
    path('programsdir/', include('MisApps.programsdir.urls')),
    path('reports/', include('MisApps.reports.urls')),
    path('students/', include('MisApps.students.urls')),
]
