from django.contrib import admin
from django.urls import path
from communityapp.views import *

urlpatterns = [
  
    path('', community, name="community"),
]