from django.urls import path,include

from flightapp import views

from  rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('flight',views.FlightViewset)
router.register('passenger',views.PassengerViewset)
router.register('reservation',views.ReservationViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('',include('rest_framework.urls')),
    path('findflight',views.find_flight),
    path('savereservation',views.save_reservation),
]

