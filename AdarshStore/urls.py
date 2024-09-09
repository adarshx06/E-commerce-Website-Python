from django.urls import path, include
from django.contrib import admin
from .views import home, signup

urlpatterns = [
    path('', home),
    path('signup', signup),
]