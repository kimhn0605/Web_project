from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('tips/', tips, name="tips"),
    path('community/', community, name="comuunity"),
    path('share/', share, name="share"),
    path('mypage/', mypage, name="mypage"),
    path('signup/', signup, name="signup"),
    path('login/', login, name="login"),
    path('login/home', home_login, name="home_login"),
    path('logout/', logout),

]