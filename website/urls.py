# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('',views.home,name='home'),
    path('home.html',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('rooms.html',views.room,name='room'),
    path('services.html',views.service,name='service'),
    path('contact.html',views.contact,name='contact'),

]
