from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


# 보험현황

class Ma000insu_list(models.Model):
    insu_name = models.TextField('보험명', max_length=100, default='변액연금보험 동행')
    insu_name02 = models.TextField('보험명', max_length=100, default='변액연금보험 동행')
    company = models.CharField('보험사', max_length=30, default='삼성')

    sell_start = models.DateField('가입일', default='2010-01-01')
    sell_end = models.DateField('가입일', default='2010-01-01')

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.insu_name

# 보험펀드 현황
class Ma001fund_list(models.Model):
    insu = models.ForeignKey(Ma000insu_list,on_delete=models.CASCADE)
    fund_code = models.CharField('펀드코드', max_length=30, default='1234')
    stock_percent = models.IntegerField('주식비중', default=10)
    fund_name = models.CharField('펀드명', max_length=30, default='주식형')
    create_date = models.DateField('설정일',default='2010-10-30')
    fund_type02 = models.CharField('펀드유형', max_length=30, default='주식형')
    input_percent = models.IntegerField('투입비율', default=10)



    def __str__(self):
        return self.fund_name

