
from django.urls import path
from account import views

urlpatterns = [

    path('register', views.register, name='register'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]
