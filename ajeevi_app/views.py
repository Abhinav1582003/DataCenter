from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
import time
from rest_framework import viewsets

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

@api_view(['GET','POST'])
def device_master_table(request):
    if request.method=='POST':
        serializer=branch_contact_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        if request.method=='GET':
            device_master_table1=device_master_table.objects.all()
            serializer=branch_contact_serializers(device_master_table1,many=True)
            return Response(serializer.data)

# it for user admin
class test_data(viewsets.ModelViewSet):
    queryset=user_admin.objects.all()
    serializer_class=user_admin_serializers

# for master table
class master_table(viewsets.ModelViewSet):
    queryset=master_table.objects.all()
    serializer_class=master_table_serializers
# address table
class address_table(viewsets.ModelViewSet):
    queryset=address.objects.all()
    serializer_class=address_serializers

# it for entityType table

class entity_table(viewsets.ModelViewSet):
    queryset=entity_type.objects.all()
    serializer_class=entity_type_serializers


# for coontact
class contact_table(viewsets.ModelViewSet):
    queryset=contact.objects.all()
    serializer_class=contact_serializers

# for branch table
class branch_table(viewsets.ModelViewSet):
    queryset=branch_table.objects.all()
    serializer_class=branch_table_serializers

# for branch address table 
class branchAddress(viewsets.ModelViewSet):
    queryset=branch_address.objects.all()
    serializer_class=branch_address_serializers

# for branch contact table
class branchContact(viewsets.ModelViewSet):
    queryset=branch_contact.objects.all()
    serializer_class=branch_contact_serializers


#device master table
class DeviceMasterTable(viewsets.ModelViewSet):
    queryset = device_master.objects.all()
    serializer_class = device_master_table_serializers

# for device part 

class device_part(viewsets.ModelViewSet):
    queryset=device_part.objects.all()
    serializer_class=device_part_serializers

# fro device location

class device_location_table(viewsets.ModelViewSet):
    queryset=device_location.objects.all()
    serilizer_class=device_location_serializers
