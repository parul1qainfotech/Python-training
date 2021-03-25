from rest_framework.throttling import UserRateThrottle

class reservationThrottle(UserRateThrottle):
    scope='reserve'