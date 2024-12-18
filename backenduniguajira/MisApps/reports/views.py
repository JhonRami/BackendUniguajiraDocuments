from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.reports.models import Reports  
from MisApps.reports.serializers import ReportsSerializer  

# Create your views here.


@api_view(['GET', 'POST'])
def reports_list(request):
    """
    List all reports, or create a new report.
    """
    if request.method == 'GET':
        reports = Reports.objects.all()  
        serializer = ReportsSerializer(reports, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReportsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def reports_detail(request, pk):
    """
    Retrieve, update or delete a report.
    """
    try:
        report = Reports.objects.get(pk=pk)  
    except Reports.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReportsSerializer(report)  
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReportsSerializer(report, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        report.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
