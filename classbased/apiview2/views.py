from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.serializers import Serializer
from rest_framework.generics import ListCreateAPIView,UpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView

class studentdata1(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer


class studentdata2(RetrieveDestroyAPIView,UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer
    

    
    

