from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth
from .models import Fuser

from django.contrib.auth import get_user_model
# Create your views here.

def home(request):
    return render(request, 'home.html')

def home_login(request) :
    return render(request, 'home_login.html')

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
            return render(request, 'home.html')
        return render(request, 'signup.html', res_data) # signup 을 요청받으면 signup.html 로 응답

def login(request): # 로그인
    
    data = {}
    response_data = ""

    if request.method == "GET" :
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            response_data = "아이디와 비밀번호를 입력해주세요."
        else : 
            try :
                myuser = Fuser.objects.get(username=login_username) 
                #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
                if check_password(login_password, myuser.password):
                    request.session['user'] = myuser.id 
                    #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                    #세션 user라는 key에 방금 로그인한 id를 저장한것.
                    return render(request, 'home_login.html', {'myuser' : myuser})
                else:
                    response_data = "아이디 혹은 비밀번호가 일치하지 않습니다."
            except Fuser.DoesNotExist:
                response_data = "아이디 혹은 비밀번호가 일치하지 않습니다."
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
    data['error'] = response_data
    return render(request, 'login.html', data)


def logout(request):
    request.session['username'] = {}
    request.session.modified = True    
    #if request.session['user'] : #로그인 중이라면
    #    del(request.session['user'])
    #return render(request, 'home.html')
    return redirect('home')


#마이페이지 구현 복붙
def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'mypage.html', context)