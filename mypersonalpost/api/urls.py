from django.urls import path,include
from api import views

urlpatterns = [
    path('posts/',views.PostList.as_view()),
    path('postCreate/',views.PostCreate.as_view()),
    path('',include('rest_framework.urls')),

]
