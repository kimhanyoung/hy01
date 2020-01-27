from django.contrib.auth.models import User
from django.db import models
import datetime


# 4. 연금예상액 (변액)
class Ma400In(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=10)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Ma400Out(models.Model):     # Pention모델 상속 + 결과화면 출력을 위하여
    gender = models.CharField('성별', max_length=5, default='남자')    #여기부터 입력분
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=1)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=2, default=7)
    public_rate = models.DecimalField('공시이율이자', max_digits=5, decimal_places=2, default=2.5)    #공시이율로는 몇 % ???
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)   #여기까지 입력분

    wholelife_annuity_10 = models.IntegerField()  # 종신연금 변액
    wholelife_annuity_20 = models.IntegerField()  # 종신연금 변액
    wholelife_annuity_80 = models.IntegerField()  # 종신연금 변액
    annuity_certain_10 = models.IntegerField()  # 확정연금 변액
    annuity_certain_15 = models.IntegerField()  # 확정연금 변액
    annuity_certain_20 = models.IntegerField()  # 확정연금 변액
    annuity_inherit = models.IntegerField()  # 상속연금 변액
    lump_sum_of_death = models.IntegerField()  # 사망시일시금 변액

    total_premium = models.IntegerField()  # 총납입금액
    reserve_money = models.IntegerField()     # 변액 준비자금
    life_table = models.CharField('경험생명표', max_length=5, default='8회')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.year


# 해지환급금
class Ma400Out01(models.Model):
    path_month = models.IntegerField('경과월', default=100)
    age = models.IntegerField('연령', default=45)
    path_year = models.IntegerField('경과년', default=10)
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_money = models.IntegerField('해지환급금', default=130000000)
    year = models.CharField('경과년월', max_length=25, default='1년')
    return_rate = models.DecimalField('환급률', max_digits=5, decimal_places=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium


# 4-1. 연금예상액 (공시이율)
class Ma600In(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=10)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)

    public_rate = models.DecimalField('공시이율이자', max_digits=5, decimal_places=1, default=2.5)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Ma600Out(models.Model):     # Pention모델 상속 + 결과화면 출력을 위하여
    gender = models.CharField('성별', max_length=5, default='남자')    #여기부터 입력분
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=1)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=2, default=7)  #변액으로는 몇 % ???
    public_rate = models.DecimalField('공시이율이자', max_digits=5, decimal_places=2, default=2.5)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)   #여기까지 입력분


    wholelife_annuity_10 = models.IntegerField()  # 종신연금 공시
    wholelife_annuity_20 = models.IntegerField()  # 종신연금 공시
    wholelife_annuity_80 = models.IntegerField()  # 종신연금 공시
    annuity_certain_10 = models.IntegerField()  # 확정연금 공시
    annuity_certain_15 = models.IntegerField()  # 확정연금 공시
    annuity_certain_20 = models.IntegerField()  # 확정연금 공시
    annuity_inherit = models.IntegerField()  # 상속연금 공시
    lump_sum_of_death = models.IntegerField()  # 사망시일시금 공시
    total_premium = models.IntegerField()  # 총납입금액
    reserve_money = models.IntegerField()   # 공시이율 준비자금

    life_table = models.CharField('경험생명표', max_length=5, default='8회')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.year

# 해지환급금
class Ma600Out01(models.Model):
    path_month = models.IntegerField('경과월', default=100)
    age = models.IntegerField('연령', default=45)
    path_year = models.IntegerField('경과년', default=10)
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_money = models.IntegerField('해지환급금', default=130000000)
    year = models.CharField('경과년월', max_length=25, default='1년')
    return_rate = models.DecimalField('환급률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.path_month
