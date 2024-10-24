from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.admission.models import Admission  
from MisApps.admission.serializers import AdmissionSerializer  

# Create your views here.


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


@api_view(['GET', 'PUT', 'DELETE'])
def admission_detail(request, pk):
    """
    Retrieve, update or delete an admission.
    """
    try:
        admission = Admission.objects.get(pk=pk)  # Cambia a Admission
    except Admission.DoesNotExist:  # Cambia a Admission
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdmissionSerializer(admission)  # Cambia a AdmissionSerializer
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdmissionSerializer(admission, data=request.data)  # Cambia a AdmissionSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        admission.delete()  # Cambia a Admission
        return Response(status=status.HTTP_204_NO_CONTENT)
