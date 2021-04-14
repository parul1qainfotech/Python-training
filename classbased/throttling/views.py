from django.shortcuts import render
from rest_framework.serializers import Serializer
from throttling.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from throttling.throttling import Userthrottle
from throttling.models import Student
from rest_framework import viewsets
from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .pagination import mypage

class ThrottlingView(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes=[SessionAuthentication]
    # throttle_classes=[AnonRateThrottle,Userthrottle,ScopedRateThrottle]
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'
    filter_backends=[DjangoFilterBackend]
    # filter_backends=[SearchFilter]
    # filter_backends=[OrderingFilter]
    # filterset_fields=['name','city']
    pagination_class= mypage
    
    