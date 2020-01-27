from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
import datetime


class Order(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')
    entry_date = models.DateField('가입일', default='2010-01-05')
    premium = models.IntegerField('월보험료', default=100)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_age = models.IntegerField('연금연령', default=65)
    transfer_date = models.IntegerField('이체일', default=10)
    entry_method = models.CharField('납입방법', max_length=30, default='적립')
    risk_premium = models.IntegerField('위험보험료', default=1000)
    count = models.IntegerField('현재 납입회차', default=0)
    payment = models.IntegerField('현재 계약자적립금', default=0)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    sign_charge7 = models.DecimalField('계약체결비용(7년 이내)', max_digits=5, decimal_places=2, default=6.06)
    sign_charge810 = models.DecimalField('계약체결비용(8년~10년)', max_digits=5, decimal_places=2, default=6.06)
    management_charge7 = models.DecimalField('관리/유지비용(7년 이내)', max_digits=7, decimal_places=2, default=5.0)
    management_charge810 = models.DecimalField('관리/유지비용(7년~10년)', max_digits=7, decimal_places=2, default=3.23)
    management_charge11 = models.DecimalField('관리/유지비용(10년 초과)', max_digits=5, decimal_places=1, default=1.5)

    sign_charge1 = models.DecimalField('계약체결비용(거치식)', max_digits=5, decimal_places=2, default=6.00)

    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

# 1. 내수익률-01 BASIC

class Aa26Fundout(models.Model):
    basic_date = models.DateField()  # 기준일자
    kospi = models.DecimalField('수정종합주가', max_digits=5, decimal_places=2)
    entry_date = models.DecimalField('가입일그래프', max_digits=5, decimal_places=2)
    fund01 = models.DecimalField('펀드01그래프', max_digits=5, decimal_places=2)
    fund02 = models.DecimalField('펀드02그래프', max_digits=5, decimal_places=2)
    fund03 = models.DecimalField('펀드03그래프', max_digits=5, decimal_places=2)
    fund04 = models.DecimalField('펀드04그래프', max_digits=5, decimal_places=2)
    fund05 = models.DecimalField('펀드05그래프', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.basic_date

#펀드그래프용 보험가입현황출력용
class Aa02Enterout(models.Model):
    entry_date = models.DateField('가입일', default='2010-01-05')
    insu_name = models.CharField('보험명', max_length=30, default='동행')
    premium = models.IntegerField('월보험료', default=100)
    paying_period = models.IntegerField('납입기간', default=10)
    transfer_date = models.IntegerField('이체일', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_age = models.IntegerField('연금연령', default=65)
    entry_method = models.CharField('납입방법', max_length=30, default='적립')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.paying_period


#펀드그래프용01
class Aa20Kospigraph(models.Model):
    date = models.DateField()  # 기준일자
    kospi = models.DecimalField('종합주가', max_digits=5, decimal_places=2)
    dow = models.DecimalField('다우', max_digits=5, decimal_places=2)
    dax = models.DecimalField('독일', max_digits=5, decimal_places=2)
    entry = models.DecimalField('가입일그래프', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.date


#펀드그래프용 07 펀드현황 출력용
class Aa02Fundout(models.Model):
    fund_no = models.CharField('펀드순번', max_length=5, default='펀드1')
    fund_name = models.CharField('펀드명', max_length=25, default='디스커버리')
    quantity = models.DecimalField('보유비중', max_digits=5, decimal_places=0)
    create_date = models.DateField()  # 생성일자
    stock_percent = models.DecimalField('주식비중', max_digits=5, decimal_places=0)
    fund_code = models.CharField('펀드코드', max_length=11, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fund_no

#펀드그래프용 -kospi 등 거치 수익률
class Aa33Kospirate(models.Model):
    entry_kospi = models.DecimalField('가입시 코스피', max_digits=5, decimal_places=2)
    entry_dow = models.DecimalField('가입시 다우', max_digits=5, decimal_places=2)
    entry_dax = models.DecimalField('가입시 독일', max_digits=5, decimal_places=2)
    present_kospi = models.DecimalField('현재 코스피', max_digits=5, decimal_places=2)
    present_dow = models.DecimalField('현재 다우', max_digits=5, decimal_places=2)
    present_dax = models.DecimalField('현재 독일', max_digits=5, decimal_places=2)

    kospi_money = models.IntegerField('코스피 평가금액', default=10000000)
    dow_money = models.IntegerField('다우 평가금액', default=10000000)
    dax_money = models.IntegerField('독일 평가금액', default=10000000)
    kospi_rate = models.DecimalField('코스피수익률', max_digits=5, decimal_places=1)
    dow_rate = models.DecimalField('다우수익률', max_digits=5, decimal_places=1)
    dax_rate = models.DecimalField('독일수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.entry_kospi

#펀드그래프용 -kospi 등 적립 수익률
class Aa37Kospiaccumrate(models.Model):
    total_premium = models.IntegerField('총납입금액', default=100000000)
    kospi_money = models.IntegerField('코스피 평가금액', default=100000000)
    dow_money = models.IntegerField('다우 평가금액', default=100000000)
    dax_money = models.IntegerField('독일 평가금액', default=100000000)
    kospi_rate = models.DecimalField('코스피수익률', max_digits=5, decimal_places=1)
    dow_rate = models.DecimalField('다우수익률', max_digits=5, decimal_places=1)
    dax_rate = models.DecimalField('독일수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium


#펀드그래프용 -과거 펀드수익률
class Aa30Fundrateout(models.Model):
    fund = models.DecimalField('펀드순번', max_digits=5, decimal_places=0)
    one_year = models.DecimalField('1년 수익률', max_digits=5, decimal_places=1)
    three_year = models.DecimalField('3년 수익률', max_digits=5, decimal_places=1)
    five_year = models.DecimalField('5년 수익률', max_digits=5, decimal_places=1)
    seven_year = models.DecimalField('7년 수익률', max_digits=5, decimal_places=1)
    ten_year = models.DecimalField('10년 수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fund


#전체펀드 평균수익률
class Aa61Totalfundaverage(models.Model):
    type = models.CharField('펀드유형', max_length=5, default='주식형')
    area = models.CharField('투자지역', max_length=5, default='국내')
    count = models.DecimalField('개수', max_digits=5, decimal_places=0)
    one_year = models.DecimalField('1년 수익률', max_digits=5, decimal_places=1)
    three_year = models.DecimalField('3년 수익률', max_digits=5, decimal_places=1)
    five_year = models.DecimalField('5년 수익률', max_digits=5, decimal_places=1)
    ten_year = models.DecimalField('10년 수익률', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.fund


#펀드상세화면 - 펀드 가입 현재 수익률
class Aa73Fundrate(models.Model):
    entry_price = models.DecimalField('가입시 기준가', max_digits=5, decimal_places=2)
    present_price = models.DecimalField('현재 기준가', max_digits=5, decimal_places=2)
    fund_money = models.IntegerField('펀드 평가금액', default=10000000)
    rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.entry_price


#펀드상세화면 - kospi 가입 현재 수익률
class Aa76Kospirate(models.Model):
    entry_price = models.DecimalField('가입시 기준가', max_digits=5, decimal_places=2)
    present_price = models.DecimalField('현재 기준가', max_digits=5, decimal_places=2)
    kospi_money = models.IntegerField('주사지수 평가금액', default=10000000)
    rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.entry_price


#펀드그래프용 -경고 편입비율, 펀드설정일
class Aa27Warning(models.Model):
    warning02 = models.CharField('설정일경고', max_length=20, default='주의')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.warning02


#수익률 - 계약자적립금
class Ab06Presentpayment(models.Model):
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_rate = models.DecimalField('수익률', max_digits=5, decimal_places=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium


# 해지환급금
class Ac02Returnmoneyout(models.Model):
    path_month = models.IntegerField('경과월', default=100)
    path_year = models.IntegerField('경과년', default=10)
    total_premium = models.IntegerField('총납입현황', default=100000000)
    payment = models.IntegerField('계약자적립금', default=130000000)
    return_money = models.IntegerField('해지환급금', default=130000000)
    year = models.CharField('경과년월', max_length=25, default='1년')
    return_rate = models.DecimalField('환급률', max_digits=5, decimal_places=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium


#연금-연금재원
class Ac03Pentionmoney(models.Model):
    total_premium = models.IntegerField('총납입현황', default=100000000)
    pention_money = models.IntegerField('연금재원', default=130000000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.total_premium


#예상연금액
class Ac04Pentionout(models.Model):
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

#수익률 - 생보해지환급금 통계
class Ab08Averageout(models.Model):
    classification = models.CharField('구분', max_length=5, default='변액연금')
    count = models.IntegerField('상품수', default=100)
    average_rate = models.DecimalField('평균연수익률', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.classification


#수익률 - 생보해지환급금 리스트출력용
class Ab07Listout(models.Model):
    company = models.CharField('회사명', max_length=20, default='동행')
    insu_name = models.CharField('보험명', max_length=20, default='동행')
    entry_date = models.DateField()  # 가입일자
    total_premium = models.IntegerField('총보험료', default=10000000)
    saved_money = models.IntegerField('계약자적립금', default=12000000)
    return_rate = models.DecimalField('환급률', max_digits=5, decimal_places=1)
    year_rate = models.DecimalField('연환산수익률', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.year_rate


#펀드상세화면을 위한 펀드선택
class Fund(models.Model):
    item = models.ForeignKey(Aa02Fundout, on_delete=models.CASCADE, null=True)
    fund_name = models.CharField(max_length=100, verbose_name='펀드명', null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.result

#펀드 상세내역 - 펀드그래프중 종합주가지수
class Aa47Graphout(models.Model):
    basic_date = models.DateField()  # 기준일자
    kospi = models.DecimalField('수정종합주가', max_digits=5, decimal_places=2)
    entry_graph = models.DecimalField('가입일그래프', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.basic_date


#펀드 상세내역 - 펀드그래프중 펀드
class Aa47Fundgraphout(models.Model):
    basic_date = models.DateField()  # 기준일자
    fund_price = models.DecimalField('펀드그래프', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.basic_date


#펀드 상세내역 02 파이그래프
class Aa48Assetout(models.Model):
    classification = models.CharField('자산명', max_length=10, default='stock')
    asset = models.DecimalField('비율', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.classification


#펀드 상세내역 03 펀드현황
class Aa49Fundout(models.Model):
    fund_code = models.CharField('펀드코드', max_length=10, default='aaa')
    fund_name = models.CharField(max_length=100, verbose_name='펀드명')
    create_date = models.DateField()  # 생성일자
    one_year = models.DecimalField('1년 수익률', max_digits=5, decimal_places=1)
    three_year = models.DecimalField('3년 수익률', max_digits=5, decimal_places=1)
    five_year = models.DecimalField('5년 수익률', max_digits=5, decimal_places=1)
    seven_year = models.DecimalField('7년 수익률', max_digits=5, decimal_places=1)
    ten_year = models.DecimalField('10년 수익률', max_digits=5, decimal_places=1)
    manage_pay = models.DecimalField('운용보수', max_digits=5, decimal_places=1)
    sell_pay = models.DecimalField('운용보수', max_digits=5, decimal_places=1)
    bank_pay = models.DecimalField('운용보수', max_digits=5, decimal_places=1)
    office_pay = models.DecimalField('운용보수', max_digits=5, decimal_places=1)
    sum_pay = models.DecimalField('운용보수', max_digits=5, decimal_places=1)
    fund_type01 = models.CharField('대유형', max_length=10, default='국내투자')
    fund_type02 = models.CharField('소유형', max_length=10, default='주식형')
    asset_money = models.IntegerField('순자산액', default=150)
    manage_company = models.CharField('운용사', max_length=100, default='미래에셋자산운용')
    stock_percent = models.DecimalField('주식비중', max_digits=5, decimal_places=0)

    def __str__(self):
        return self.fund_code


#펀드 상세내역 04 적립식수익률
class Aa53Accumulrate(models.Model):
    count = models.DecimalField('납입회차', max_digits=5, decimal_places=0)
    total_premium = models.IntegerField('총납입금액', default=10000000)
    kospi_money = models.IntegerField('주사지수 평가금액', default=10000000)
    fund_money = models.IntegerField('펀드 평가금액', default=10000000)
    kospi_rate = models.DecimalField('kospi 1년 수익률', max_digits=5, decimal_places=1)
    fund_rate = models.DecimalField('펀드 1년 수익률', max_digits=5, decimal_places=1)

    def __str__(self):
        return self.kospi_rate


# 3. 적립식펀드
class Fund03In(models.Model):
    entry_date = models.DateField('가입일', default='2009-01-05')  # 가입일자
    premium = models.IntegerField('가입금액', default=10000)
    fund_type = models.CharField('펀드유형', max_length=5, default='주식형')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Fund05List(models.Model):     # 뷰 출력분
    date = models.DateField()  # 기준일자
    modify_price = models.DecimalField('수정기준가', max_digits=5, decimal_places=2)
    tex_price = models.DecimalField('과표기준가', max_digits=5, decimal_places=2)
    kospi = models.DecimalField('수정종합주가', max_digits=5, decimal_places=2)
    tex_graph = models.DecimalField('결산그래프', max_digits=5, decimal_places=2)
    entry_graph = models.DecimalField('가입일그래프', max_digits=5, decimal_places=2)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.date


class Fund06Tex(models.Model):  # 뷰 출력분
    tex_date = models.DateField()  # 결산일
    tex_price = models.DecimalField('과표기준가', max_digits=5, decimal_places=2)
    tex = models.IntegerField('1억당이자소득세', default=100000)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.tex_date


class Fund09Result(models.Model):  # 뷰 출력분
    entry_price = models.DecimalField('가입시기준가', max_digits=5, decimal_places=2)
    present_price = models.DecimalField('현재기준가', max_digits=5, decimal_places=2)
    earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2)
    tex_earning_rate = models.DecimalField('과표수익률', max_digits=5, decimal_places=2)
    earning = models.IntegerField('소득세', default=100000)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.entry_price

class Fund10Entry(models.Model):  # 뷰 출력분
    entry_date = models.DateField('가입일', default='2010-01-05')  # 가입일자
    premium = models.IntegerField('가입금액', default=10000)
    fund_type = models.CharField('펀드유형', max_length=5, default='주식형')
    fund_name = models.CharField('펀드명', max_length=50)
    warning = models.CharField('경고', max_length=50, null=True)


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.entry_date

