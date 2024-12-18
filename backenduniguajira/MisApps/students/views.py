from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.students.models import Students  
from MisApps.students.serializers import StudentsSerializer  

# Create your views here.


@api_view(['GET', 'POST'])
def students_list(request):
    """
    List all students, or create a new student.
    """
    if request.method == 'GET':
        students = Students.objects.all()  
        serializer = StudentsSerializer(students, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def students_detail(request, pk):
    """
    Retrieve, update or delete a student.
    """
    try:
        student = Students.objects.get(pk=pk)  
    except Students.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(student)  
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentsSerializer(student, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
