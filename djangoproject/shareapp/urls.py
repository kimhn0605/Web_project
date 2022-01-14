from django.contrib import admin
from django.urls import path
from shareapp.views import *

urlpatterns = [
  
    path('', share, name="share"),
]