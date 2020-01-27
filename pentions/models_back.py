from django.contrib.auth.models import User
from django.db import models
import datetime


class Pention(models.Model):                   #연금 부모클래스
    reserve_money = models.IntegerField()         #책임준비금
    wholelife_annuity_10 = models.IntegerField()  # 종신연금
    wholelife_annuity_20 = models.IntegerField()  # 종신연금
    wholelife_annuity_80 = models.IntegerField()  # 종신연금
    annuity_certain_10 = models.IntegerField()  # 확정연금
    annuity_certain_15 = models.IntegerField()  # 확정연금
    annuity_certain_20 = models.IntegerField()  # 확정연금
    annuity_inherit = models.IntegerField()  # 상속연금
    lump_sum_of_death = models.IntegerField()  # 사망시일시금

    class Meta:            #적용은 안되게하는 코드   추상클래스(부모) : Meta=True 를 지정해주면 실제로 데이타베시스는 만들어지지 않고
        abstract = True       #자식클래스에 상속+ 추가필드 자식클래스에 넣으면 된다

#적립식사업비 필드(변액)
#sign_charge7 = models.DecimalField('계약체결비용(7년 이내)', max_digits=4, decimal_places=2, default=4.70)
#sign_charge810 = models.DecimalField('계약체결비용(8년~10년)', max_digits=4, decimal_places=2,default=3.36)
#management_charge7 = models.DecimalField('관리/유지비용(7년 이내)', max_digits=7, decimal_places=2,default=3.87)
#management_charge810 = models.DecimalField('관리/유지비용(7년~10년)', max_digits=7, decimal_places=2,default=4.50)
#management_charge11 = models.DecimalField('관리/유지비용(10년 초과)', max_digits=7, decimal_places=2,default=1.54)

#거치식사업비 필드
#sign_charge1 = models.DecimalField('계약체결비용(1차월)', max_digits=4, decimal_places=2, default=1.52)
#sign_charge2 = models.DecimalField('계약체결비용(2차월 이후)', max_digits=4, decimal_places=2, default=0.05)
#management_charge1 = models.DecimalField('관리/유지비용(1차월)', max_digits=7, decimal_places=2,default=0.96)
#management_charge2 = models.DecimalField('관리/유지비용(2차월 이후)', max_digits=7, decimal_places=2,default=0.04)

# 1. 투자의 원칙(1)시간의 가치
class Ma100In(models.Model):
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간',help_text='5,7,10,12,15,10년납 중 선택', default=10)
    earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=7.0)
    chulsu_start_year = models.IntegerField('철수시작', default=10)
    result_year = models.IntegerField('결과보기', default=30)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.premium

class Ma100Out(models.Model):     # 입력분+출력분
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=7)
    chulsu_start_year = models.IntegerField('철수시작', default=10)
    result_year = models.IntegerField('결과보기', default=30)
    year = models.IntegerField()           #여기부터출력분
    younghee_total_premium = models.IntegerField()  # 영희총납입금액
    chulsu_total_premium = models.IntegerField()  # 철수총납입금액
    chulsu_surrender_value = models.IntegerField()  # 철수해약환급금
    younghee_surrender_value = models.IntegerField()  # 영희해약환급금
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)     #

    def __str__(self):
        return self.year

class Ma100Out02(models.Model):     # 입력분+출력분
    younghee_total_premium = models.IntegerField()  # 영희총납입금액
    younghee_surrender_value = models.IntegerField()  # 영희해약환급금
    younghee_rate = models.DecimalField('영희수익률', max_digits=5, decimal_places=2, default=7)
    chulsu_total_premium = models.IntegerField()  # 철수총납입금액
    chulsu_surrender_value = models.IntegerField()  # 철수해약환급금
    chulsu_rate = models.DecimalField('영희수익률', max_digits=5, decimal_places=2, default=7)
    gap = models.IntegerField()  # 영희 철수 해약환급금 차이

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)     #

    def __str__(self):
        return self.gap

# 2. 투자의 원칙(2) 수익률
class Ma200In(models.Model):
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    younghee_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=10)
    chulsu_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=7)
    result_year = models.IntegerField('결과보기', default=30)

    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.premium

class Ma200Out(models.Model):  # 입력분+출력분
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    younghee_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=10)
    chulsu_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=7)
    result_year = models.IntegerField('결과보기', default=30)
    year = models.IntegerField()                                         # 여기부터출력분
    total_premium = models.IntegerField()  # 총납입금액
    chulsu_surrender_value = models.IntegerField()  # 철수해약환급금
    younghee_surrender_value = models.IntegerField()  # 영희해약환급금
    difference = models.IntegerField()  # 차액

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.year

class Ma200Out02(models.Model):     # 입력분+출력분
    total_premium = models.IntegerField()  # 총납입금액
    younghee_surrender_value = models.IntegerField()  # 영희해약환급금
    younghee_rate = models.DecimalField('영희수익률', max_digits=5, decimal_places=2, default=7)
    chulsu_surrender_value = models.IntegerField()  # 철수해약환급금
    chulsu_rate = models.DecimalField('영희수익률', max_digits=5, decimal_places=2, default=7)
    gap = models.IntegerField()  # 영희 철수 해약환급금 차이

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)     #

    def __str__(self):
        return self.gap


# 3. 투자의 원칙(3) 세금
class Ma300In(models.Model):
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    younghee_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=7)
    chulsu_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=5)
    result_year = models.IntegerField('결과보기', default=30)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Ma300Out(models.Model):  # 입력분+출력분
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    younghee_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=7)
    chulsu_earning_rate = models.DecimalField('수익률', max_digits=5, decimal_places=2, default=5)
    result_year = models.IntegerField('결과보기', default=30)
    year = models.IntegerField()                                        # 여기부터출력분
    total_premium = models.IntegerField()  # 총납입금액
    chulsu_surrender_value = models.IntegerField()  # 철수해약환급금
    chulsu_tax = models.IntegerField()  # 철수세금
    chulsu_tax_after = models.IntegerField()  # 철수세후
    younghee_surrender_value = models.IntegerField()  # 영희해약환급금
    younghee_tax = models.IntegerField()  # 영희세금
    younghee_tax_after = models.IntegerField()  # 영희세후

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #

    def __str__(self):
        return self.year

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


# 6. 연금예상액(일시금)
class Mc100In(models.Model):
    life_expectancy = models.IntegerField('기대여명', default=90)
    gender = models.CharField('성별', max_length=5, default='남자')
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)
    reserve_money = models.IntegerField('준비자금', default=100000000)
    present_age = models.IntegerField('현재연령', default=45)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.gender

class Mc100Out(models.Model):                       #
    life_expectancy = models.IntegerField('기대여명', default=90, null=True)
    gender = models.CharField('성별', max_length=5, default='남자', null=True)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0, null=True)
    present_age = models.IntegerField('현재연령', default=45, null=True)
    reserve_money = models.IntegerField('준비자금', default=100000000, null=True)

    wholelife_annuity_10 = models.IntegerField(null=True)  # 종신연금
    wholelife_annuity_20 = models.IntegerField(null=True)  # 종신연금
    wholelife_annuity_80 = models.IntegerField(null=True)  # 종신연금
    annuity_certain_10 = models.IntegerField(null=True)  # 확정연금
    annuity_certain_15 = models.IntegerField(null=True)  # 확정연금
    annuity_certain_20 = models.IntegerField(null=True)  # 확정연금
    annuity_inherit = models.IntegerField(null=True)  # 상속연금
    lump_sum_of_death = models.IntegerField(null=True)  # 사망시일시금

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #

    def __str__(self):
        return self.life_expectancy



# 7. 연금목표 월납입액
class Mc200In(models.Model):
    target_pention = models.IntegerField('월 목표연금액', default=3000000)
    gender = models.CharField('성별', max_length=5, default='남자')
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    public_rate = models.DecimalField('공시이율이자', max_digits=5, decimal_places=1, default=2.5)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Mc200Out(models.Model):     #
    target_pention = models.IntegerField('월 목표연금액', default=3000000)
    gender = models.CharField('성별', max_length=5, default='남자')
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    public_rate = models.DecimalField('공시이율이자', max_digits=5, decimal_places=1, default=2.5)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)   # 여기까지 입력분

    variable_monthly_premium = models.IntegerField()  # 변액월납입금액    #출력분
    public_monthly_premium = models.IntegerField()  # 공시월납입금액
    variable_total_premium = models.IntegerField()  # 변액총납입금액
    public_total_premium = models.IntegerField()  # 공시총납입금액
    reserve_money = models.IntegerField()   # 준비자금
    total_pention = models.IntegerField()  # 연금 총수령액(100세기준)
    variable_output_rate = models.IntegerField()  # 변액수령비율
    public_output_rate = models.IntegerField()  # 공시 수령비율

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.year


# 8. 연금개시후 공시이율
class Mc300In(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=10)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    first_pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=5.0)
    second_pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Mc300Out01(models.Model):     #첫번째 이자 연금
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=10)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)
    first_pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=5.0)
    second_pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)  #입력분

    first_wholelife_annuity_10 = models.IntegerField()  # 종신연금 첫째
    first_wholelife_annuity_20 = models.IntegerField()  # 종신연금 첫째
    first_wholelife_annuity_80 = models.IntegerField()  # 종신연금 첫째
    first_annuity_certain_10 = models.IntegerField()  # 확정연금 첫째
    first_annuity_certain_15 = models.IntegerField()  # 확정연금 첫째
    first_annuity_certain_20 = models.IntegerField()  # 확정연금 첫째
    first_annuity_inherit = models.IntegerField()  # 상속연금 첫째
    first_lump_sum_of_death = models.IntegerField()  # 사망시일시금 첫째

    reserve_money = models.IntegerField()  # 책임준비금

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #

    def __str__(self):
        return self.year

class Mc300Out02(models.Model):     #두번째 이자 연금
    second_wholelife_annuity_10 = models.IntegerField()  # 종신연금 두번째
    second_wholelife_annuity_20 = models.IntegerField()  # 종신연금 두번째
    second_wholelife_annuity_80 = models.IntegerField()  # 종신연금 두번째
    second_annuity_certain_10 = models.IntegerField()  # 확정연금 두번째
    second_annuity_certain_15 = models.IntegerField()  # 확정연금 두번째
    second_annuity_certain_20 = models.IntegerField()  # 확정연금 두번째
    second_annuity_inherit = models.IntegerField()  # 상속연금 두번째
    second_lump_sum_of_death = models.IntegerField()  # 사망시일시금 두번째

    reserve_money = models.IntegerField()  # 책임준비금
    life_table = models.CharField('경험생명표', max_length=5, default='8회')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #

    def __str__(self):
        return self.year


# 9. 변액연금비용
class Md100In(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=10)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)


    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Md100Out(models.Model):     # Pention모델 상속 + 결과화면 출력을 위하여
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=1)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    earning_rate = models.DecimalField('변액수익률', max_digits=5, decimal_places=1, default=7.0)   #입력분

    total_premium = models.IntegerField()  # 총납입금액
    reserve_money = models.IntegerField()  # 책임준비금
    life_table = models.CharField('경험생명표', max_length=5, default='8회')
    total_gmab = models.IntegerField()  # 총gmab
    gmab_rate = models.IntegerField()  # 총납입금액 대비
    present_gmab = models.IntegerField()  # 현재까지 gmab
    future_gmab = models.IntegerField()  # 연금개시전 gmab
    wholelife_annuity_20 = models.IntegerField()  #종신연금
    total_wholelife_annuity_20 = models.IntegerField()  # 종신연금 total
    management_fee = models.IntegerField()  # 연금개시전 gmab

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.gender

class Md100Out01(models.Model):     # 그래프용
    classification = models.CharField('구분', max_length=5, default='gmab', null=True)
    result = models.IntegerField()  # 종신연금 total

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.classification


# 10. 위험보험료
class Md200In(models.Model):
    risk_premium = models.IntegerField('위험보험료', default=1000)
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=1)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Md200Out(models.Model):  #  결과화면 출력을 위하여
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=1)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    risk_premium = models.IntegerField('위험보험료', default=1000)      # 입력분

    age = models.IntegerField()  # 연령
    age_premium = models.IntegerField()  # 연령별 납입보험료
    age_risk_premium = models.IntegerField()  # 연령별 위험보험료
    premium_risk_rate = models.IntegerField()   #납입금액 대비
    total_risk_premium = models.IntegerField()   # 연금개시전 총위험보험료
    averige_risk_premium = models.IntegerField()  # 월평균 총위험보험료

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #


    def __str__(self):
        return self.gender


# 적금의 비밀
class Mg100In(models.Model):
    deposit_rate = models.DecimalField('적금이자', max_digits=5, decimal_places=1, default=2.0)
    premium = models.IntegerField('적금액', default=1000000)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Mg100Out(models.Model):     # 결과화면 출력을 위하여
    deposit_rate = models.DecimalField('적금이자', max_digits=5, decimal_places=1, default=2.0)
    premium = models.IntegerField('적금액', default=1000000)   #입력분

    pass_month = models.IntegerField()  # 경과월
    rate_money = models.IntegerField()  #이자액
    real_rate = models.IntegerField()  # 실이자
    total_rate_money = models.IntegerField()  # 총이자액
    total_real_rate = models.IntegerField()  # 총실질이자
    tax = models.IntegerField()  # 세금
    after_money = models.IntegerField()  # 세후이자액
    after_real_rate = models.IntegerField()  # 세후 실질이자

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #

    def __str__(self):
        return self.premium

#  수익률별 연금예상액
class Mh200In(models.Model):
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=10)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    a_earning_rate = models.DecimalField('a원장 님수익률', max_digits=5, decimal_places=2, default=7)
    b_earning_rate = models.DecimalField('b원장님 수익률', max_digits=5, decimal_places=2, default=5)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)

    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.premium

class Mh200Out(models.Model):  # 입력분+출력분
    gender = models.CharField('성별', max_length=5, default='남자')
    start_year = models.IntegerField('납입년', default=2010)
    start_month = models.IntegerField('납입월', default=1)
    premium = models.IntegerField('월보험료', default=1000000)
    paying_period = models.IntegerField('납입기간', default=10)
    present_age = models.IntegerField('현재연령', default=45)
    pention_start_age = models.IntegerField('연금개시연령', default=65)
    a_earning_rate = models.DecimalField('a원장 님수익률', max_digits=5, decimal_places=2, default=7.0)
    b_earning_rate = models.DecimalField('b원장님 수익률', max_digits=5, decimal_places=2, default=4.0)
    pention_start_rate = models.DecimalField('연금개시시이율', max_digits=3, decimal_places=1, default=2.0)   #입력분

    a_wholelife_annuity_10 = models.IntegerField()  # 종신연금 a원장님
    a_wholelife_annuity_20 = models.IntegerField()  # 종신연금 a원장님
    a_wholelife_annuity_80 = models.IntegerField()  # 종신연금 a원장님
    a_annuity_certain_10 = models.IntegerField()  # 확정연금 a원장님
    a_annuity_certain_15 = models.IntegerField()  # 확정연금 a원장님
    a_annuity_certain_20 = models.IntegerField()  # 확정연금 a원장님
    a_annuity_inherit = models.IntegerField()  # 상속연금 a원장님
    a_lump_sum_of_death = models.IntegerField()  # 사망시일시금 a원장님
    b_wholelife_annuity_10 = models.IntegerField()  # 종신연금 b원장님
    b_wholelife_annuity_20 = models.IntegerField()  # 종신연금 b원장님
    b_wholelife_annuity_80 = models.IntegerField()  # 종신연금 b원장님
    b_annuity_certain_10 = models.IntegerField()  # 확정연금 b원장님
    b_annuity_certain_15 = models.IntegerField()  # 확정연금 b원장님
    b_annuity_certain_20 = models.IntegerField()  # 확정연금 b원장님
    b_annuity_inherit = models.IntegerField()  # 상속연금 b원장님
    b_lump_sum_of_death = models.IntegerField()  # 사망시일시금 b원장님
    total_premium = models.IntegerField()  # 총납입금액
    b_reserve_money = models.IntegerField()  # b원장님이율 준비자금
    a_reserve_money = models.IntegerField()  # a원장님 준비자금

    life_table = models.CharField('경험생명표', max_length=5, default='8회')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #

    def __str__(self):
        return self.gender
