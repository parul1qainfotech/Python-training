from django.shortcuts import render
from rest_framework import generics
from .models import Post,Vote
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from post.serializers import PostSerializer,VoteSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import ValidationError

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    authenticated_classes=[BaseAuthentication]
    
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
        
class Votecreate(generics.CreateAPIView):
    serializer_class=VoteSerializer
    permission_classes=[IsAuthenticated]
    authenticated_classes=[BaseAuthentication]
    
    def get_queryset(self):
        user=self.request.user
        post=Post.objects.get(id=self.kwargs['id'])   
        return Vote.objects.filter(voter=user,post=post)  
    
    def perform_create(self,serializer):
        if self.get_queryset().exists():
            raise ValidationError('already voted for this post')
        serializer.save(voter=self.request.user,post=Post.objects.get(id=self.kwargs['id']))   
    
    
