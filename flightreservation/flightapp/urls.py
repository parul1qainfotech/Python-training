from django.urls import path,include

from flightapp import views

from  rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views


router=DefaultRouter()
router.register('flight',views.FlightViewset)
router.register('passenger',views.PassengerViewset)
router.register('reservation',views.ReservationViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('',include('rest_framework.urls')),
    path('findflight',views.find_flight),
    path('savereservation',views.save_reservation),
    path('api_auth_token/',obtain_auth_token),
    path('jwtget/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwtrefresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('jwtverify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]

