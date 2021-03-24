from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import filters

from flightapp.models import Flight,Passenger,Reservation
from flightapp.serializers import FlightSerailizer,PassengerSerializer,ReservationSerializer



@api_view(['POST'])
def find_flight(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'],
                                  arrivalCity=request.data['arrivalCity'],
                                  dateOfDeparture=request.data['dateOfDeparture']
                                  )
    serializer=FlightSerailizer(flights,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['id'])
    passenger=Passenger()
    passenger.firstName=request.data['firstName']
    passenger.lastName=request.data['lastName']
    passenger.middleName=request.data['middleName']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()
    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger=passenger
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewset(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerailizer
    filter_backends = [filters.SearchFilter]
    search_fields=['id','departureCity','arrivalCity','operatingAirline']


class PassengerViewset(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields=['firstName','lastName','middleName','email']


class ReservationViewset(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
