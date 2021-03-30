from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework import status
from django.db import IntegrityError
from io import BytesIO

from api.serializers import (TodoSerializer,
                            TodoUpdateSerializer,
                            TodoUpdateUrgentField,
                            UserSerializer)
from todo.models import ToDo

# @csrf_exempt
# def signup(request):
#     if request.method == 'POST':
#         try:
#             user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#             user.save()
#             return JsonResponse({'token':'successfull'},status=status.HTTP_201_CREATED)
#         except IntegrityError:
#             return JsonResponse({'error':'the username already taken'},status=status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

        
#for retreiving the completed list of todo of authenticated users
class TodoCompletedList(generics.ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]

    def get_queryset(self):
        user=self.request.user
        return ToDo.objects.filter(user=user,completed__isnull=False).order_by('-completed')
   
#for create todo for authenticated user and get the created todo
class TodoCreateList(generics.ListCreateAPIView):
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]

    def get_queryset(self):
        user=self.request.user
        return ToDo.objects.filter(user=user,completed__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
     
#for update,delete and retrieve the todo for authenticated user based on id
class TodoRetrieveUpdateDeleteList(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]
  
    def get_queryset(self):
        user=self.request.user
        return ToDo.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
#for marking the todo to be completed (update the todo)
class TodoCompleteUpdate(generics.UpdateAPIView):
    serializer_class=TodoUpdateSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]

    def get_queryset(self):
        user=self.request.user
        return ToDo.objects.filter(user=user)
 
    def perform_update(self, serializer):
        serializer.instance.completed=timezone.now()
        serializer.save()
       
#for marking the todo to be urgent (update the todo) 
class TodoUrgentmark(generics.RetrieveUpdateAPIView):
    serializer_class=TodoUpdateUrgentField
    permission_classes=[IsAuthenticated]
    authentication_classes=[SessionAuthentication]

    def get_queryset(self):
        user=self.request.user
        return ToDo.objects.filter(user=user)
