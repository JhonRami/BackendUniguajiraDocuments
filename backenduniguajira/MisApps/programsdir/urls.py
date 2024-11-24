from django.urls import path
from MisApps.admission import views
from MisApps.programsdir import views
from MisApps.programsdir.viewsbasic import programsdir_detail, programsdir_list
urlpatterns = [
    path('', programsdir_list),
    path('<int:pk>/', programsdir_detail),
    path('listado/', views.admission_list, name='admission-list'), #admissions/
    path('query1/', views.admission_query1, name='admission_query1'), #admissions/query1/
    path('query2/', views.admission_query2, name='admission_query2'), #admissions/query2/
    path('query3/', views.loans_query1, name='loans_query1'),              #loans/query1/
    path('query4/', views.reports_query1, name='reports_query1'),        #reports/query1/
    path('query5/', views.students_grouped, name='students_grouped'),  #students/grouped/
    path('query6/', views.professors_grouped, name='professors_grouped'), #professors/grouped
]
