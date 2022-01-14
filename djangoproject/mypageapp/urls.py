from django.contrib import admin
from django.urls import path
from mypageapp.views import *

urlpatterns = [
  
    path('', mypage, name="mypage"),
]