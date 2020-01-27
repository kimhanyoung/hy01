from django.db import models
from django.contrib.auth.models import User
import datetime

from django.urls import reverse

class Ae00Input(models.Model):
    classification = models.CharField('구분', max_length=7, default='종합주가')
    start_date = models.DateField('시작일', default='1996-01-05')  # 펀드변경검증 시작일
    end_date = models.DateField('종료일', default='2019-08-20')  # 펀드변경검증 종료일

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.start_date

# 고객선택내역 출력용
class Ae01Out(models.Model):
    classification = models.CharField('구분', max_length=7, default='종합주가')
    start_date = models.DateField('시작일', default='1996-01-05')  # 펀드변경검증 시작일
    end_date = models.DateField('종료일', default='2019-08-20')  # 펀드변경검증 종료일

    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.start_date


#펀드변경결과 출력용01
class Ae05Result(models.Model):
    classification = models.CharField('구분', max_length=10, default='종합주가지수')
    start_date = models.DateField('시작일', default='2005-01-05')
    end_date = models.DateField('종료일', default='2019-01-05')
    accum_premium = models.IntegerField('적립총보험료', default=100000000)
    defer_premium = models.IntegerField('거치보험료', default=100000000)

    accum_stock_count = models.DecimalField('적립주식좌수', max_digits=5, decimal_places=2, null=True)
    accum_bond_count = models.DecimalField('적립채권좌수', max_digits=5, decimal_places=2, null=True)
    defer_stock_count = models.DecimalField('거치주식좌수', max_digits=5, decimal_places=2, null=True)
    defer_bond_count = models.DecimalField('거치채권좌수', max_digits=5, decimal_places=2, null=True)
    accum_count = models.DecimalField('그냥주식좌수', max_digits=5, decimal_places=2, null=True)
    defer_count = models.DecimalField('그냥채권좌수', max_digits=5, decimal_places=2, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.classification

#펀드변경결과 출력용02
class Ae05Result01(models.Model):
    stock_start_price = models.DecimalField('주식 시작 기준가', max_digits=5, decimal_places=2)
    stock_end_price = models.DecimalField('주식 종료 기준가', max_digits=5, decimal_places=2)
    stock_rate = models.DecimalField('주식상승률', max_digits=5, decimal_places=1, null=True)

    bond_start_price = models.DecimalField('채권 시작 기준가', max_digits=5, decimal_places=2)
    bond_end_price = models.DecimalField('채권 종료 기준가', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.classification

#펀드변경 그래프
class Ae10Graph(models.Model):
    classification = models.CharField('구분', max_length=10, default='종합주가')
    date = models.DateField('날자', default='2005-01-05')
    stock = models.DecimalField('주식 기준가', max_digits=5, decimal_places=2)
    bond = models.DecimalField('채권 기준가', max_digits=5, decimal_places=2)
    stock_change = models.DecimalField('주식변경그래프', max_digits=5, decimal_places=2)
    bond_change = models.DecimalField('채권변경그래프', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.classification

    class Meta:
        ordering = ['date']


#펀드변경 시작 끝 그래프
class Ae11Startend(models.Model):
    date = models.DateField('날자', default='2005-01-05')
    start = models.DecimalField('시작일 그래프', max_digits=5, decimal_places=2)
    end = models.DecimalField('끝 그래프', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.date

#펀드변경 숫자
class Ae13Count(models.Model):
    stock_count = models.DecimalField('주식변경개수', max_digits=5, decimal_places=0)
    bond_count = models.DecimalField('채권변경개수', max_digits=5, decimal_places=0)
    total_count = models.DecimalField('총변경개수', max_digits=5, decimal_places=0)

    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.start_date

# 펀드변경 통계 입력용
class Af01input(models.Model):
    path_month = models.IntegerField('경과년', default=15)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

#펀드변경결과 통계 출력용
class Af07Result(models.Model):
    classification = models.CharField('구분', max_length=10, default='종합주가지수')
    accum_premium = models.IntegerField('적립총보험료', default=100000000)
    defer_premium = models.IntegerField('거치보험료', default=100000000)

    accum_stock = models.IntegerField('적립그냥주식평가금액', default=100000000)
    accum_stock_rate = models.DecimalField('적립그냥주식수익률', max_digits=5, decimal_places=1)
    accum_change = models.IntegerField('적립펀번주식평가금액', default=100000000)
    accum_change_rate = models.DecimalField('적립펀번주식수익률', max_digits=5, decimal_places=1)
    accum_rate_gap = models.DecimalField('적립수익률차이', max_digits=5, decimal_places=1, null=True)

    defer_stock = models.IntegerField('거치그냥주식평가금액', default=100000000)
    defer_stock_rate = models.DecimalField('거치그냥주식수익률', max_digits=5, decimal_places=1)
    defer_change = models.IntegerField('거치펀번평가금액', default=100000000)
    defer_change_rate = models.DecimalField('거치펀번수익률', max_digits=5, decimal_places=1)
    defer_rate_gap = models.DecimalField('거치수익률차이', max_digits=5, decimal_places=1, null=True)
    total_count = models.DecimalField('총검증개수', max_digits=5, decimal_places=0, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.classification


#펀드변경 통계 시작 끝 그래프
class Af14Graph(models.Model):
    date = models.DateField('날자', default='2005-01-05')
    kospi = models.DecimalField('종합주가 그래프', max_digits=5, decimal_places=2)
    reverse_kospi = models.DecimalField('역종합 그래프', max_digits=5, decimal_places=2)
    start = models.DecimalField('투자시작 그래프', max_digits=5, decimal_places=2)
    end = models.DecimalField('투자끝 그래프', max_digits=5, decimal_places=2)
    zero = models.DecimalField('0그래프', max_digits=5, decimal_places=2, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.date


#펀드변경 문자
class Ag00Fundalarm(models.Model):
    date = models.DateField('날자', default='2005-01-05')
    fund_type = models.CharField('편드타입', max_length=10, default='주식형유지')
    content = models.TextField('내용', default='종합주가')

    def __str__(self):
        return self.date