from rest_framework.throttling import UserRateThrottle

class  Userthrottle(UserRateThrottle):
    scope='jack'