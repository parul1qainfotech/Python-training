from django.shortcuts import render
from viewset.models import Student
from viewset.serializers import StudentSerializer
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class viewsetdata(viewsets.ViewSet):
    def list(self,request,):
        print('*****list*******')
        print('basename',self.basename)
        print('action',self.action)
        print('detial',self.detail)
        print('suffix',self.suffix)
        print('name',self.name)
        print('description',self.description)
        print('***************************')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        if pk is not None:
            print('*****Retrieve*******')
            print('basename',self.basename)
            print('action',self.action)
            print('detial',self.detail)
            print('suffix',self.suffix)
            print('name',self.name)
            print('description',self.description)
            print('***************************')
            data=Student.objects.get(id=pk)
            Serializer=StudentSerializer(data)
            return Response(Serializer.data,status=status.HTTP_200_OK)
    
    
    
    def put(self,request,pk=None):
        if pk is not None:
            data=Student.objects.get(id=pk)
            Serializer=StudentSerializer(data,data=request.data)
            if Serializer.is_valid():
                Serializer.save()
                return Response(Serializer.data,status=status.HTTP_200_OK)
            return Response(Serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,pk=None):
        if pk is not None:
            data=Student.objects.get(id=pk)
            Serializer=StudentSerializer(data,data=request.data,partial=True)
            if Serializer.is_valid():
                Serializer.save()
                return Response(Serializer.data,status=status.HTTP_200_OK)
            return Response(Serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        data=Student.objects.get(id=pk)
        data.delete()
        return Response({'msg':'deleted successfully '},status=status.HTTP_200_OK)
        
        
        
