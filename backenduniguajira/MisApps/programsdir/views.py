from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Q, Count
from MisApps.admission.models import Admission
from MisApps.admission.serializers import AdmissionSerializer
from MisApps.loans.models import Loans
from MisApps.loans.serializers import LoansSerializer
from MisApps.reports.models import Reports
from MisApps.reports.serializers import ReportsSerializer
from MisApps.students.models import Students
from MisApps.professors.models import Professors

# View to list and create Admissions
@api_view(['GET', 'POST'])
def admission_list(request):
    """
    List all admissions, or create a new admission.
    """
    if request.method == 'GET':
        admissions = Admission.objects.all()
        serializer = AdmissionSerializer(admissions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View for basic query - Admissions with conditions
@api_view(['GET'])
def admission_query1(request):
    """
    Query 1: Admissions with basic conditions.
    """
    admissions = Admission.objects.filter(
        Q(status="activo") & 
        Q(dateadmission__year=2023)
    )
    serializer = AdmissionSerializer(admissions, many=True)
    return Response(serializer.data)


# View for query with body parameters - Admissions
@api_view(['GET'])
def admission_query2(request):
    """
    Query 2: Admissions with conditions from body parameters.
    """
    status = request.data.get('status', None)
    year = request.data.get('year', None)
    query = Q()

    if status:
        query &= Q(status__icontains=status)
    if year:
        query &= Q(dateadmission__year=year)

    admissions = Admission.objects.filter(query)
    serializer = AdmissionSerializer(admissions, many=True)
    return Response(serializer.data)


# View for complex conditions - Loans
@api_view(['GET'])
def loans_query1(request):
    """
    Query 3: Loans with complex conditions.
    """
    loans = Loans.objects.filter(
        Q(dateloans__year=2024) &
        (Q(datereturn__isnull=True) | Q(namebook__icontains="Cold"))
    )
    serializer = LoansSerializer(loans, many=True)
    return Response(serializer.data)


# View for text conditions - Reports
@api_view(['GET'])
def reports_query1(request):
    """
    Query 4: Reports with text conditions.
    """
    reports = Reports.objects.filter(
        Q(description__icontains="warning") | 
        Q(date__year=2024)
    )
    serializer = ReportsSerializer(reports, many=True)
    return Response(serializer.data)


# View for grouping Students by program
@api_view(['GET'])
def students_grouped(request):
    """
    Query 5: Group students by program.
    """
    students = Students.objects.values('program__name').annotate(total=Count('id'))
    return Response(students)


# View for professors grouped by program with conditions
@api_view(['GET'])
def professors_grouped(request):
    """
    Query 6: Group professors by program with conditions.
    """
    professors = Professors.objects.filter(
        program__name__icontains="Nice"
    ).values(
        'program__name'
    ).annotate(
        total=Count('id')
    )
    return Response(professors)
