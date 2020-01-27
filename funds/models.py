from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


# 펀드현황

class Ma000fund_list(models.Model):
    fund_name = models.TextField('펀드명', max_length=100, default='디스커버리')
    fund_code = models.CharField('펀드코드', max_length=30, default='1234')
    company = models.CharField('운용사', max_length=30, default='미래에셋')
    fund_type = models.CharField('펀드유형', max_length=30, default='주식형')
    create_date = models.DateField('설정일', default='2010-10-02')
    area_section = models.CharField('펀드구분', max_length=30, default='국내')

    fund_money_million = models.IntegerField('설정액 백만원', default=0)
    fund_money_hunmillion = models.IntegerField('설정액 억', default=0)
    manage_pay = models.DecimalField('운용보수', max_digits=3, decimal_places=1, default=0)
    sell_pay = models.DecimalField('판매보수', max_digits=3, decimal_places=1, default=0)
    bank_pay = models.DecimalField('수탁보수', max_digits=3, decimal_places=1, default=0)
    office_pay = models.DecimalField('사무관리보수', max_digits=3, decimal_places=1, default=0)
    total_pay = models.DecimalField('총보수', max_digits=3, decimal_places=1, default=0)
    averige_pay = models.DecimalField('보수평균', max_digits=3, decimal_places=1, default=0)
    before_charge = models.DecimalField('선취수수료', max_digits=3, decimal_places=1, default=0)
    after_charge = models.DecimalField('후취수수료', max_digits=3, decimal_places=1, default=0)
    modify_date = models.DateTimeField('업데이트일자', auto_now=True)

    entry_date = models.DateField('가입일', default='2010-10-02')
    transfer_date = models.IntegerField('이체일', default= 10)
    entry_money = models.IntegerField('가입금액', default= 1000000 )
    entry_method = models.CharField('납입방법', max_length=30, default='적립')

#    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.fund_name

# 펀드명 검색
class Fa100In(models.Model):
    fund_name = models.CharField('펀드명', max_length=30, default='디스커버리')
    company = models.CharField('운용사', max_length=30, default='미래에셋')
    fund_type = models.CharField('펀드유형', max_length=30, default='주식형')
    area_section = models.CharField('펀드구분', max_length=30, default='국내')

#    owner = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.fund_name


class Fa100Out(models.Model):  # 입력분+출력분
    fund_name = models.CharField('펀드명', max_length=30, default='디스커버리')
    company = models.CharField('운용사', max_length=30, default='미래에셋')
    fund_type = models.CharField('펀드유형', max_length=30, default='주식형')
    area_section = models.CharField('펀드구분', max_length=30, default='국내')    #입력분

    fund_name_list = models.CharField('펀드명', max_length=30, default='디스커버리')
    company_list = models.CharField('운용사', max_length=30, default='미래에셋')
    fund_type_list = models.CharField('펀드유형', max_length=30, default='주식형')
    area_section_list = models.CharField('펀드구분', max_length=30, default='국내')
    create_date = models.DateField('설정일', default='2010-10-02')

    def __str__(self):
        return self.year

    class Meta:
        managed = False
        db_table = 'Funds_Fa100Out'  # 서버의 뷰 이름


