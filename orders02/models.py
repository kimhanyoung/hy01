from django.contrib.auth.models import User
from django.db import models
import datetime

class Ad00Input(models.Model):
    count = models.IntegerField('납입회차', default=100)
    payment = models.IntegerField('계약자적립금', default=100000000)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.count

# 해지환급금
class Ad03Returnmoneyout(models.Model):
    path_month = models.IntegerField('경과월', default=100)
    age = models.IntegerField('연령', default=45)
    path_year = models.IntegerField('경과년', default=10)
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_money = models.IntegerField('해지환급금', default=130000000)
    year = models.CharField('경과년월', max_length=25, default='1년')
    return_rate = models.DecimalField('환급률', max_digits=5, decimal_places=1)
    expect_rate = models.DecimalField('예상수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium

    class Meta:
        managed = False  # 필드변경시 True 로 바꿔서 마이그레이트
        db_table = 'Orders02_Ad03Returnmoneyout'  # 서버의 뷰 이름

class Ad06Enterout(models.Model):
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)
    count = models.IntegerField('경과월수', default=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium

    class Meta:
        managed = False                   #필드변경시 True 로 바꿔서 마이그레이트
        db_table = 'Orders02_Ad06Enterout'  # 서버의 뷰 이름

#연금-연금재원
class Ad04Pentionmoney(models.Model):
    total_premium = models.IntegerField('총납입현황', default=100000000)
    pention_money = models.IntegerField('연금재원', default=130000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium

    class Meta:
        managed = False                   #필드변경시 True 로 바꿔서 마이그레이트
        db_table = 'Orders02_Ad04Pentionmoney'  # 서버의 뷰 이름


#예상연금액
class Ad05Pentionout(models.Model):
    whole_10 = models.IntegerField('상속연금10년보증', default=130000000)
    whole_20 = models.IntegerField('상속연금20년보증', default=130000000)
    whole_80 = models.IntegerField('상속연금80세보증', default=130000000)
    set_10 = models.IntegerField('10년확정', default=130000000)
    set_15 = models.IntegerField('15년확정', default=130000000)
    set_20 = models.IntegerField('20년확정', default=130000000)
    inherit_month = models.IntegerField('상속연금', default=130000000)
    inherit_lumpsum = models.IntegerField('상속일시금', default=130000000)
    total_whole_10 = models.IntegerField('총상속연금10년보증', default=130000000)
    total_whole_20 = models.IntegerField('총상속연금20년보증', default=130000000)
    total_whole_80 = models.IntegerField('총상속연금80세보증', default=130000000)
    total_set_10 = models.IntegerField('총10년확정', default=130000000)
    total_set_15 = models.IntegerField('총15년확정', default=130000000)
    total_set_20 = models.IntegerField('총20년확정', default=130000000)
    total_inherit_month = models.IntegerField('총상속연금', default=130000000)
    total_premium = models.IntegerField('총납입보험료', default=130000000)
    pention_money = models.IntegerField('연금개시재원', default=130000000)
    return_rate = models.DecimalField('환급률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.whole_10

    class Meta:
        managed = False                   #필드변경시 True 로 바꿔서 마이그레이트
        db_table = 'Orders02_Ad05Pentionout'  # 서버의 뷰 이름
