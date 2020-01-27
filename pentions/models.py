from django.contrib.auth.models import User
from django.db import models
import datetime


# 5. 경험생명표별 연금액
class Ma500In(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')

    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.5)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Ma500Out(models.Model):  #
    gender = models.CharField('성별', max_length=5, default='남자')

    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=5.0)  # 입력분

    annuity_certain_10 = models.IntegerField()  # 확정연금 10년형 회차별 동일

    three_wholelife_annuity_20 = models.IntegerField()  # 3회 종신연금
    four_wholelife_annuity_20 = models.IntegerField()  # 4회 종신연금
    five_wholelife_annuity_20 = models.IntegerField()  # 5회 종신연금
    six_wholelife_annuity_20 = models.IntegerField()  # 6회 종신연금
    seven_wholelife_annuity_20 = models.IntegerField()  # 7회 종신연금
    eight_wholelife_annuity_20 = models.IntegerField()  # 8회 종신연금

    vs_four_wholelife_annuity_20 = models.IntegerField()  # 3회 대비 종신연금
    vs_five_wholelife_annuity_20 = models.IntegerField()  # 3회 대비 종신연금
    vs_six_wholelife_annuity_20 = models.IntegerField()  # 3회 대비 종신연금
    vs_seven_wholelife_annuity_20 = models.IntegerField()  # 3회 대비 종신연금
    vs_eight_wholelife_annuity_20 = models.IntegerField()  # 3회 대비 종신연금

    total_three_wholelife_annuity_20 = models.IntegerField()  # 3회 종신연금 total
    total_four_wholelife_annuity_20 = models.IntegerField()  # 4회 종신연금 total
    total_five_wholelife_annuity_20 = models.IntegerField()  # 5회 종신연금 total
    total_six_wholelife_annuity_20 = models.IntegerField()  # 6회 종신연금 total
    total_seven_wholelife_annuity_20 = models.IntegerField()  # 7회 종신연금 total
    total_eight_wholelife_annuity_20 = models.IntegerField()  # 8회 종신연금 total

    reserve_money = models.IntegerField()  # 책임준비금
    total_premium = models.IntegerField()  # 총납입금액

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.year



