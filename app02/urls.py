from django.contrib import admin
from django.urls import path, include
from app02 import views

urlpatterns = [
    path('index/', views.index, name="ind"),
    path('order/', views.order, name="ord"),
    path('login/', views.login),
]