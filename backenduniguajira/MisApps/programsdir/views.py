from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.programsdir.models import Programsdir  
from MisApps.programsdir.serializers import ProgramsdirSerializer  

# Create your views here.


@api_view(['GET', 'POST'])
def programsdir_list(request):
    """
    List all programsdir, or create a new programsdir.
    """
    if request.method == 'GET':
        programsdir = Programsdir.objects.all()  
        serializer = ProgramsdirSerializer(programsdir, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProgramsdirSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def programsdir_detail(request, pk):
    """
    Retrieve, update or delete a programsdir.
    """
    try:
        programdir = Programsdir.objects.get(pk=pk)  
    except Programsdir.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProgramsdirSerializer(programdir)  
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProgramsdirSerializer(programdir, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        programdir.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
