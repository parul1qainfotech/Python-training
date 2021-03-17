from modelserial.models import Details
from rest_framework import serializers

class DetailSerializer(serializers.ModelSerializer):
    def validate_data(self,value):
        name=value.get('name')
        roll=value.get('roll')
        if name and roll is not None:
            raise serializers.ValidationError('This is super user data please enter other')
    name=serializers.CharField(validators=[validate_data])
    class Meta:
        model=Details
        fields=['id','name','age','roll','city']
    
        read_only_fields=['name','roll']
        
        
        
        
        