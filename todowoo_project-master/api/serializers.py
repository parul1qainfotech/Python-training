from rest_framework import serializers
from todo.models import ToDo
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    class Meta:
        model=ToDo
        fields=['id','title','memo','created_at','urgent','completed','created_at']
  
class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields=['id']
        read_only_fields=['title','memo','created_at','urgent','completed','created_at']

class TodoUpdateUrgentField(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields=['id','urgent'] 
        read_only_fields=['title','memo','created_at','completed','created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
