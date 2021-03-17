from rest_framework import serializers
from api.models import Student
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=70)
    
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    
    
    def validate_roll(self,value):
        if value.get('roll')==145:
            raise serializers.ValidationError('error')
        return value
    
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.city=validate_data.get('city',instance.city)
        instance.save()
        return instance

    
    
    
