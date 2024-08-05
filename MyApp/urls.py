from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.index, name= 'MyApp'),
    path("about",views.about, name= 'about'),
    path("products",views.services, name= 'products'),
    path("contact",views.contacts, name= 'contact'),
    path("Android",views.services, name= 'Android'),
    path("ios",views.services, name= 'ios'),
    path("Hard_disk",views.services, name= 'Hard_disk')
]