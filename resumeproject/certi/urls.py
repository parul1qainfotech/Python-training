from django.urls import path
from . import views

urlpatterns = [
    path('certificate/', views.certificates,name="certificate"),
]