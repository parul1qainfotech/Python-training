from django.shortcuts import render
from api.models import Post,Like
from api.serializers import PostSerializer,LikeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import PagePagination
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth.models import User

class PostList(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes=[SessionAuthentication]
    filter_backends=[filters.SearchFilter]
    search_fields = ['id', 'title']
                
class PostCreate(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    pagination_class=PagePagination
    permission_classes=[IsAuthenticatedOrReadOnly]
    authentication_classes=[SessionAuthentication]
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['id']
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
    

        
            
            
            
    
    
    





