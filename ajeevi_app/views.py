from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
import time


@api_view(['GET','POST'])
def test_data(request):
    if request.method =='POST':
        serializer=user_admin_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        if request.method=='GET':
            user_admin1=user_admin.objects.all()
            serializer=user_admin_serializers(user_admin1,many=True)
            return Response(serializer.data)   


@api_view(['GET','POST'])
def master_table_data(request):
    if request.method=='POST':
        serializer=master_table_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method=='GET':
         master_table1=master_table.objects.all()
         serializer=master_table_serializers(master_table1,many=True)
         return Response(serializer.data)


@api_view(['GET','POST'])
def address_table(request):
    if request.method=='POST':
         serializer=address_serializers(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         else:
            return Response(serializer.errors)
    if request.method=='GET':
         address_table1=address.objects.all()
         serializer=address_serializers(address_table1,many=True)
         return Response(serializer.data)        
    

@api_view(['GET','POST'])
def entity_type_table(request):
    if request.method=='POST':
        serializer=entity_type_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method=='GET':
        entity_type1=entity_type.objects.all()
        serializer=entity_type_serializers(entity_type1,many=True)
        return Response(serializer.data)        

@api_view(['GET','POST'])
def contact_table(request):
    if request.method =='POST':
        serializer=contact_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        if request.method=='GET':
            contact_table1=contact.objects.all()
            serializer=contact_serializers(contact_table1,many=True)
            return Response(serializer.data)  



@api_view(['GET','POST'])
def branch_table_data(request):
    if request.method=='POST':
        serializer=branch_table_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        if request.method=='GET':
            branch_table1=contact.objects.all()
            serializer=branch_table_serializers(branch_table1,many=True)
            return Response(serializer.data)              


@api_view(['GET','POST'])
def branch_address_table(request):
    if request.method=='POST':
        serializer=branch_address_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        if request.method=='GET':
            branch_address1=branch_address.objects.all()
            serializer=branch_table_serializers(branch_address1,many=True)
            return Response(serializer.data) 
        

@api_view(['GET','POST'])
def branch_contact_table(request):
    if request.method=='POST':
        serializer=branch_contact_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else: 
        if request.method=='GET':
            branch_contact1=branch_contact.objects.all()
            serializer=branch_contact_serializers(branch_contact1,many=True)
            return Response(serializer.data) 
       