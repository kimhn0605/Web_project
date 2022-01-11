from django.shortcuts import render
from .models import Fuser
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tips(request):
    return render(request, 'tips.html')

def community(request):
    return render(request, 'community.html')

def share(request):
    return render(request, 'share.html')


def mypage(request):
    return render(request, 'mypage.html')