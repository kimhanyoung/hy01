from django.contrib.auth.models import User
from django.db import models
import datetime

class Aa01Input(models.Model):
    birth_date = models.DateField('생년월일', default='1996-01-10')     #생년월일
    end_date = models.DateField('종료일', default='2019-08-10')       #종료일(현재)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.birth_date

# 화면출력용 뷰
class Aa02Insuage(models.Model):
    insu_age = models.IntegerField('경과월', default=100)
    birth_date = models.DateField('생년월일', default='1996-01-10')  # 생년월일
    end_date = models.DateField('종료일', default='2019-08-10')  # 종료일(현재)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.insu_age

