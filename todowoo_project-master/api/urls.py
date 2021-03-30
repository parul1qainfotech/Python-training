from django.urls import path ,include

from api import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('todos/completed/',views.TodoCompletedList.as_view()),
    path('todos/create/',views.TodoCreateList.as_view()),
    path('todos/upatedeleteretireve/<int:pk>/',views.TodoRetrieveUpdateDeleteList.as_view()),
    path('todos/markcompleted/<int:pk>/',views.TodoCompleteUpdate.as_view()),
    path('todos/urgentupdate/<int:pk>/',views.TodoUrgentmark.as_view()),
    path('register', views.UserCreate.as_view()),
    
    path('',include('rest_framework.urls')),
]
