"""classbased URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from apivieww import views
from apiview2 import views as v
# from viewset import views as vs
from modelviewset import views as vm
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
# router.register('studentviewset',vs.viewsetdata,basename='viewset')
router.register('studentmodelviewset',vm.modelviewsetdata,basename='modelviewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentdata/',views.StudentDetails2.as_view()),
    # path('studentdata/<int:pk>/',views.StudentDetails1.as_view()),
    path('studentdata/',v.studentdata1.as_view()),
    path('studentdata/<int:pk>/',v.studentdata2.as_view()),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    
]
