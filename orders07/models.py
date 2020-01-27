from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Metfund(models.Model):
    fund_name = models.CharField(max_length=200, db_index=True)
    fund_code = models.CharField(max_length=200, null=True)
    create_date = models.DateField('설정일', default='2010-10-02', null=True)
    fund_type01 = models.CharField('펀드유형', max_length=30, default='국내투자', null=True)
    fund_type02 = models.CharField('펀드유형', max_length=30, default='주식형', null=True)
    stock_percent = models.IntegerField(null=True)
    count = models.IntegerField('편입비율', null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fund_name


#펀드 편입비율 합계 - 처음 펀드수정화면에서 보여주기
class Aa01Totalcount(models.Model):
    total_count = models.IntegerField('총 편입비율', default=100)
    amount = models.IntegerField('펀드개수', default=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_count


#수익률 - 현재 계약자적립금
class Aa07Presentpayment(models.Model):
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium


# 예상수익률 보여주기
class Aa08Expectrate(models.Model):
    expect_rate = models.DecimalField('예상수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.expect_rate


#예상연금액
class Aa12Pentionout(models.Model):
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

# 펀드그래프
class Ab02fundprice(models.Model):
    count = models.IntegerField('일련번호', null=True)
    fund_code = models.CharField(max_length=200, null=True)
    date = models.DateField('기준일자', default='2010-10-02', null=True)
    price = models.DecimalField('기준가', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.count

# 코스피그래프
class Ab03kospigraph(models.Model):
    count = models.IntegerField('일련번호', null=True)
    fund_code = models.CharField(max_length=200, null=True)
    date = models.DateField('기준일자', default='2010-10-02', null=True)
    price = models.DecimalField('기준가', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.count

# 가입일그래프
class Ab04entrygraph(models.Model):
    count = models.IntegerField('일련번호', null=True)
    fund_code = models.CharField(max_length=200, null=True)
    date = models.DateField('기준일자', default='2010-10-02', null=True)
    price = models.DecimalField('기준가', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.count

#고객가입펀드 수익률
class Ac03Fundrate(models.Model):
    fund_name = models.CharField(max_length=200, db_index=True)
    entry_price = models.DecimalField('가입시 기준가', max_digits=5, decimal_places=2)
    present_price = models.DecimalField('현재 기준가', max_digits=5, decimal_places=2)
    fund_money = models.IntegerField('펀드 평가금액', default=10000000)
    rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.entry_price

# 고객선택(BM) 펀드 수익률
class Ac06Metrate(models.Model):
    fund_name = models.CharField(max_length=200, db_index=True)
    entry_price = models.DecimalField('가입시 기준가', max_digits=5, decimal_places=2)
    present_price = models.DecimalField('현재 기준가', max_digits=5, decimal_places=2)
    fund_money = models.IntegerField('펀드 평가금액', default=10000000)
    rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)
    fund_no = models.IntegerField('펀드no', default=4)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.entry_price

