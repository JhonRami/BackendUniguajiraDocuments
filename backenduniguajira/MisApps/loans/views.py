from django.shortcuts import render
from django.http import Http404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

from MisApps.loans.models import Loans  
from MisApps.loans.serializers import LoansSerializer  

# Create your views here.


@api_view(['GET', 'POST'])
def loans_list(request):
    """
    List all loans, or create a new loan.
    """
    if request.method == 'GET':
        loans = Loans.objects.all()  
        serializer = LoansSerializer(loans, many=True) 
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoansSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def loans_detail(request, pk):
    """
    Retrieve, update or delete a loan.
    """
    try:
        loan = Loans.objects.get(pk=pk)  
    except Loans.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoansSerializer(loan)  
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoansSerializer(loan, data=request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)
