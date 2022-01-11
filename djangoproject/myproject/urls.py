from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    
    path('tips/', tips, name="tips"),
    
    path('community/', community, name="comuunity"),
    
    path('share/', share, name="share"),
    path('mypage/', mypage, name="mypage"),
    path('signup/', signup, name="signup"),
    
]