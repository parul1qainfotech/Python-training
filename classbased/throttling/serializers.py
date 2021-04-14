from rest_framework import serializers
from viewset.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']

