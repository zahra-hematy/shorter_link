from django.contrib import admin
from django.urls import path
from .views import ConvertView





urlpatterns = [
    path('', ConvertView, name='home'),
]
