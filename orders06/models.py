from django.contrib.auth.models import User
from django.db import models
import datetime

# 흥부와 놀부  -- 둘다 listview
class HungbuOut(models.Model):
    date = models.DateField()  # 기준일자
    kospi = models.DecimalField('종합주가지수', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.date

    class Meta:
        managed = False
        db_table = 'orders06_HungbuOut'  # 서버의 뷰 이름

class HungbuOut02(models.Model):  # 결과화면 출력을 위하여
    date = models.DateField()  # 기준일자
    kospi = models.DecimalField('종합주가지수', max_digits=5, decimal_places=2)
    hungbu_entry_date = models.DateField()  # 흥부가입일자
    nolbu_entry_date = models.DateField()  # 놀부가입일자
    hungbu_pention_start_date = models.DateField()  # 흥부 연금개시일자
    nolbu_pention_start_date = models.DateField()  # 놀부 연금개시일자

    def __str__(self):
        return self.date

