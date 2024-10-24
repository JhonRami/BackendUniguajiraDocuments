from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.professors.models import Professors  
from MisApps.professors.serializers import ProfessorsSerializer  

# Create your views here.


@api_view(['GET', 'POST'])
def professors_list(request):
    """
    List all professors, or create a new professor.
    """
    if request.method == 'GET':
        professors = Professors.objects.all()  
        serializer = ProfessorsSerializer(professors, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfessorsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def professors_detail(request, pk):
    """
    Retrieve, update or delete a professor.
    """
    try:
        professor = Professors.objects.get(pk=pk)  
    except Professors.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfessorsSerializer(professor)  
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfessorsSerializer(professor, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        professor.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
