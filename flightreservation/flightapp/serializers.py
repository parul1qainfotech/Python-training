from rest_framework import serializers
import re
from flightapp.models import Flight,Passenger,Reservation
from rest_framework.validators import UniqueValidator,UniqueTogetherValidator

class FlightSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'
        validators=[UniqueValidator(queryset=Flight.objects.all())]
        
    def validate_flightNumber(self,flightNumber):
        if(re.match("^[a-zA-Z0-9]*$",flightNumber)==None):
            raise serializers.ValidationError("Flightnumber should be alpha numeric only ")
        return flightNumber
    

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields='__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Passenger.objects.all(),
                fields=['email','phone']
            )
        ]

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'