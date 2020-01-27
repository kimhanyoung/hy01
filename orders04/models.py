from django.contrib.auth.models import User
from django.db import models
import datetime

class Aa00Input(models.Model):
    start_date = models.DateField('시작일', default='2000-01-10')     #가입일
    end_date = models.DateField('종료일', default='2019-08-10')       #종료일(현재)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.start_date

# 화면출력용 뷰
class Aa01Pathmonth(models.Model):
    path_month = models.IntegerField('경과월', default=100)
    start_date = models.DateField('시작일', default='2000-01-10')  # 가입일
    end_date = models.DateField('종료일', default='2019-08-10')  # 종료일(현재)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.path_month



