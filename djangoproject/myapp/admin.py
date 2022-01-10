from django.contrib import admin
from .models import Fuser

# Register your models here.

class FuserAdmin(admin.ModelAdmin): #admin의 ModelAdmin 클래스를 상속
    pass #상속만 받아 새로운 클래스를 생성

admin.site.register(Fuser,FuserAdmin) #admin 페이지에 등록