from django.shortcuts import render
from modelviewset.models import Student
from modelviewset.serializers import StudentSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
from .permissions import Mypermission
# Create your views here.

class modelviewsetdata(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[Mypermission]
