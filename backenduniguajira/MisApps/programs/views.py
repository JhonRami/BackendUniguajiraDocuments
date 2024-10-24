from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.programs.models import Programs  
from MisApps.programs.serializers import ProgramsSerializer  

# Create your views here.


@api_view(['GET', 'POST'])
def programs_list(request):
    """
    List all programs, or create a new program.
    """
    if request.method == 'GET':
        programs = Programs.objects.all()  
        serializer = ProgramsSerializer(programs, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProgramsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def programs_detail(request, pk):
    """
    Retrieve, update or delete a program.
    """
    try:
        program = Programs.objects.get(pk=pk)  
    except Programs.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProgramsSerializer(program)  
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProgramsSerializer(program, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        program.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
