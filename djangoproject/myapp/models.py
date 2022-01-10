from django.contrib.admin.decorators import register
from django.db import models
from django.db.models.base import Model

# Create your models here.

class Fuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='syw')#'사용자명'admin 페이지에 보일 컬럼명
    password = models.CharField(max_length=64,
                                verbose_name='1234')#'비밀번호'admin 페이지에 보일 컬럼명
    register_dttm = models.DateField(auto_now_add=True,
                                    verbose_name="가입날짜") #'가입날짜'자동으로 해당시간 추가됨

    #데이터가 문자열로 변환이 될 때 어떻게 나올지(반환해줄지) 정의하는 함수
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'user_define_fuser_table' #테이블 명 지정
        verbose_name = '사용자 모임' # 노출될 테이블 이름 변경
        verbose_name_plural = '사용자 모임'