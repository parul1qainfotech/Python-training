from django.contrib import admin

from flightapp.models import Flight,Passenger,Reservation


# Register your models here.
@admin.register(Flight)
class AdminFlight(admin.ModelAdmin):
    list_display=['flightNumber','operatingAirline','departureCity','arrivalCity','dateOfDeparture','estimatedTimeOfDeparture']

@admin.register(Passenger)
class AdminPassenger(admin.ModelAdmin):
    list_display=['firstName','lastName','middleName','email','phone']
        
@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display=['flight','passenger']