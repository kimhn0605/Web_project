from django.contrib import admin
from django.urls import path
from tipsapp.views import *

urlpatterns = [
  
    path('', tips, name="tips"),
]