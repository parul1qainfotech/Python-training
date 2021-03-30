from django.contrib import admin
from django.urls import path,include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Todos
    path('todos/', views.todos, name='todos'),
    path('completedtodos/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('create/', views.createtodo, name='createtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),


    #API
    path('api/',include('api.urls'))
]
