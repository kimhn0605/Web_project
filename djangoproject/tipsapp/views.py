from django.shortcuts import render

# Create your views here.

def tips(request):
    return render(request, 'tips.html')
