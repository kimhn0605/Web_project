from django.shortcuts import render
from django.contrib.auth.hashers import make_password
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

def signup(request):          # 회원가입 페이지를 보여주기str위한HTML함수
    if request.method == "GET" :
        return render(request, 'signup.html')

    elif request.method == "POST" :
        username = request.POST.get('username')   
        email = request.POST.get('email', None)
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        
        res_data = {} 
        if password != re_password :
            res_data['error'] = '비밀번호가 다릅니다.'
        
        if not (username and email and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        else :
            fuser = Fuser(
                username = username, 
                password = make_password(password), 
                email = email,
            )
            fuser.save()
        return render(request, 'signup.html', res_data) # signup 을 요청받으면 signup.html 로 응답