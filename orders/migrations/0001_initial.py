# Generated by Django 2.0.13 on 2019-10-26 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0026_delete_product05'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aa02Enterout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default='2010-01-05', verbose_name='가입일')),
                ('insu_name', models.CharField(default='동행', max_length=30, verbose_name='보험명')),
                ('premium', models.IntegerField(default=100, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('transfer_date', models.IntegerField(default=10, verbose_name='이체일')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('pention_age', models.IntegerField(default=65, verbose_name='연금연령')),
                ('entry_method', models.CharField(default='적립', max_length=30, verbose_name='납입방법')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa02Fundout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_no', models.CharField(default='펀드1', max_length=5, verbose_name='펀드순번')),
                ('fund_name', models.CharField(default='디스커버리', max_length=25, verbose_name='펀드명')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='보유비중')),
                ('create_date', models.DateField()),
                ('stock_percent', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='주식비중')),
                ('fund_code', models.CharField(default='', max_length=11, verbose_name='펀드코드')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa20Kospigraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('kospi', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='종합주가')),
                ('dow', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='다우')),
                ('dax', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='독일')),
                ('entry', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입일그래프')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa26Fundout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_date', models.DateField()),
                ('kospi', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='수정종합주가')),
                ('entry_date', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입일그래프')),
                ('fund01', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='펀드01그래프')),
                ('fund02', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='펀드02그래프')),
                ('fund03', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='펀드03그래프')),
                ('fund04', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='펀드04그래프')),
                ('fund05', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='펀드05그래프')),
            ],
        ),
        migrations.CreateModel(
            name='Aa27Warning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning02', models.CharField(default='주의', max_length=20, verbose_name='설정일경고')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa30Fundrateout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='펀드순번')),
                ('one_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='1년 수익률')),
                ('three_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='3년 수익률')),
                ('five_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='5년 수익률')),
                ('seven_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='7년 수익률')),
                ('ten_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='10년 수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa33Kospirate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_kospi', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 코스피')),
                ('entry_dow', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 다우')),
                ('entry_dax', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 독일')),
                ('present_kospi', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 코스피')),
                ('present_dow', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 다우')),
                ('present_dax', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 독일')),
                ('kospi_money', models.IntegerField(default=10000000, verbose_name='코스피 평가금액')),
                ('dow_money', models.IntegerField(default=10000000, verbose_name='다우 평가금액')),
                ('dax_money', models.IntegerField(default=10000000, verbose_name='독일 평가금액')),
                ('kospi_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='코스피수익률')),
                ('dow_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='다우수익률')),
                ('dax_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='독일수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa37Kospiaccumrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_premium', models.IntegerField(default=100000000, verbose_name='총납입금액')),
                ('kospi_money', models.IntegerField(default=100000000, verbose_name='코스피 평가금액')),
                ('dow_money', models.IntegerField(default=100000000, verbose_name='다우 평가금액')),
                ('dax_money', models.IntegerField(default=100000000, verbose_name='독일 평가금액')),
                ('kospi_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='코스피수익률')),
                ('dow_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='다우수익률')),
                ('dax_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='독일수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aa47Fundgraphout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_date', models.DateField()),
                ('fund_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='펀드그래프')),
            ],
        ),
        migrations.CreateModel(
            name='Aa47Graphout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_date', models.DateField()),
                ('kospi', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='수정종합주가')),
                ('entry_graph', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입일그래프')),
            ],
        ),
        migrations.CreateModel(
            name='Aa48Assetout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(default='stock', max_length=10, verbose_name='자산명')),
                ('asset', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='비율')),
            ],
        ),
        migrations.CreateModel(
            name='Aa49Fundout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(default='aaa', max_length=10, verbose_name='펀드코드')),
                ('fund_name', models.CharField(max_length=100, verbose_name='펀드명')),
                ('create_date', models.DateField()),
                ('one_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='1년 수익률')),
                ('three_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='3년 수익률')),
                ('five_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='5년 수익률')),
                ('seven_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='7년 수익률')),
                ('ten_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='10년 수익률')),
                ('manage_pay', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='운용보수')),
                ('sell_pay', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='운용보수')),
                ('bank_pay', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='운용보수')),
                ('office_pay', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='운용보수')),
                ('sum_pay', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='운용보수')),
                ('fund_type01', models.CharField(default='국내투자', max_length=10, verbose_name='대유형')),
                ('fund_type02', models.CharField(default='주식형', max_length=10, verbose_name='소유형')),
                ('asset_money', models.IntegerField(default=150, verbose_name='순자산액')),
                ('manage_company', models.CharField(default='미래에셋자산운용', max_length=100, verbose_name='운용사')),
                ('stock_percent', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='주식비중')),
            ],
        ),
        migrations.CreateModel(
            name='Aa53Accumulrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='납입회차')),
                ('total_premium', models.IntegerField(default=10000000, verbose_name='총납입금액')),
                ('kospi_money', models.IntegerField(default=10000000, verbose_name='주사지수 평가금액')),
                ('fund_money', models.IntegerField(default=10000000, verbose_name='펀드 평가금액')),
                ('kospi_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='kospi 1년 수익률')),
                ('fund_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='펀드 1년 수익률')),
            ],
        ),
        migrations.CreateModel(
            name='Aa61Totalfundaverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='주식형', max_length=5, verbose_name='펀드유형')),
                ('area', models.CharField(default='국내', max_length=5, verbose_name='투자지역')),
                ('count', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='개수')),
                ('one_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='1년 수익률')),
                ('three_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='3년 수익률')),
                ('five_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='5년 수익률')),
                ('ten_year', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='10년 수익률')),
            ],
        ),
        migrations.CreateModel(
            name='Aa73Fundrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 기준가')),
                ('present_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 기준가')),
                ('fund_money', models.IntegerField(default=10000000, verbose_name='펀드 평가금액')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='수익률')),
            ],
        ),
        migrations.CreateModel(
            name='Aa76Kospirate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 기준가')),
                ('present_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 기준가')),
                ('kospi_money', models.IntegerField(default=10000000, verbose_name='주사지수 평가금액')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='수익률')),
            ],
        ),
        migrations.CreateModel(
            name='Ab06Presentpayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_premium', models.IntegerField(default=100000000, verbose_name='총납입현황')),
                ('payment', models.IntegerField(default=130000000, verbose_name='계약자적립금')),
                ('return_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab07Listout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='동행', max_length=20, verbose_name='회사명')),
                ('insu_name', models.CharField(default='동행', max_length=20, verbose_name='보험명')),
                ('entry_date', models.DateField()),
                ('total_premium', models.IntegerField(default=10000000, verbose_name='총보험료')),
                ('saved_money', models.IntegerField(default=12000000, verbose_name='계약자적립금')),
                ('return_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='환급률')),
                ('year_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='연환산수익률')),
            ],
        ),
        migrations.CreateModel(
            name='Ab08Averageout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(default='변액연금', max_length=5, verbose_name='구분')),
                ('count', models.IntegerField(default=100, verbose_name='상품수')),
                ('average_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='평균연수익률')),
            ],
        ),
        migrations.CreateModel(
            name='Ac02Returnmoneyout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_month', models.IntegerField(default=100, verbose_name='경과월')),
                ('age', models.IntegerField(default=45, verbose_name='연령')),
                ('path_year', models.IntegerField(default=10, verbose_name='경과년')),
                ('total_premium', models.IntegerField(default=100000000, verbose_name='총납입현황')),
                ('payment', models.IntegerField(default=130000000, verbose_name='계약자적립금')),
                ('return_money', models.IntegerField(default=130000000, verbose_name='해지환급금')),
                ('year', models.CharField(default='1년', max_length=25, verbose_name='경과년월')),
                ('return_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='환급률')),
                ('expect_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='예상수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ac03Pentionmoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_premium', models.IntegerField(default=100000000, verbose_name='총납입현황')),
                ('pention_money', models.IntegerField(default=130000000, verbose_name='연금재원')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ac04Pentionout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whole_10', models.IntegerField(default=130000000, verbose_name='상속연금10년보증')),
                ('whole_20', models.IntegerField(default=130000000, verbose_name='상속연금20년보증')),
                ('whole_80', models.IntegerField(default=130000000, verbose_name='상속연금80세보증')),
                ('set_10', models.IntegerField(default=130000000, verbose_name='10년확정')),
                ('set_15', models.IntegerField(default=130000000, verbose_name='15년확정')),
                ('set_20', models.IntegerField(default=130000000, verbose_name='20년확정')),
                ('inherit_month', models.IntegerField(default=130000000, verbose_name='상속연금')),
                ('inherit_lumpsum', models.IntegerField(default=130000000, verbose_name='상속일시금')),
                ('total_whole_10', models.IntegerField(default=130000000, verbose_name='총상속연금10년보증')),
                ('total_whole_20', models.IntegerField(default=130000000, verbose_name='총상속연금20년보증')),
                ('total_whole_80', models.IntegerField(default=130000000, verbose_name='총상속연금80세보증')),
                ('total_set_10', models.IntegerField(default=130000000, verbose_name='총10년확정')),
                ('total_set_15', models.IntegerField(default=130000000, verbose_name='총15년확정')),
                ('total_set_20', models.IntegerField(default=130000000, verbose_name='총20년확정')),
                ('total_inherit_month', models.IntegerField(default=130000000, verbose_name='총상속연금')),
                ('total_premium', models.IntegerField(default=130000000, verbose_name='총납입보험료')),
                ('pention_money', models.IntegerField(default=130000000, verbose_name='연금개시재원')),
                ('return_rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='환급률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_name', models.CharField(max_length=100, null=True, verbose_name='펀드명')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Aa02Fundout')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund03In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default='2010-01-05', verbose_name='가입일')),
                ('premium', models.IntegerField(default=10000, verbose_name='가입금액')),
                ('fund_type', models.CharField(default='주식형', max_length=5, verbose_name='펀드유형')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund05List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('modify_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='수정기준가')),
                ('tex_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='과표기준가')),
                ('kospi', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='수정종합주가')),
                ('tex_graph', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='결산그래프')),
                ('entry_graph', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입일그래프')),
            ],
        ),
        migrations.CreateModel(
            name='Fund06Tex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tex_date', models.DateField()),
                ('tex_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='과표기준가')),
                ('tex', models.IntegerField(default=100000, verbose_name='1억당이자소득세')),
            ],
        ),
        migrations.CreateModel(
            name='Fund09Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시기준가')),
                ('present_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재기준가')),
                ('earning_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='수익률')),
                ('tex_earning_rate', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='과표수익률')),
                ('earning', models.IntegerField(default=100000, verbose_name='소득세')),
            ],
        ),
        migrations.CreateModel(
            name='Fund10Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default='2010-01-05', verbose_name='가입일')),
                ('premium', models.IntegerField(default=10000, verbose_name='가입금액')),
                ('fund_type', models.CharField(default='주식형', max_length=5, verbose_name='펀드유형')),
                ('fund_name', models.CharField(max_length=50, verbose_name='펀드명')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='남자', max_length=5, verbose_name='성별')),
                ('entry_date', models.DateField(default='2010-01-05', verbose_name='가입일')),
                ('premium', models.IntegerField(default=100, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('pention_age', models.IntegerField(default=65, verbose_name='연금연령')),
                ('transfer_date', models.IntegerField(default=10, verbose_name='이체일')),
                ('entry_method', models.CharField(default='적립', max_length=30, verbose_name='납입방법')),
                ('risk_premium', models.IntegerField(default=1000, verbose_name='위험보험료')),
                ('count', models.IntegerField(default=0, verbose_name='현재 납입회차')),
                ('payment', models.IntegerField(default=0, verbose_name='현재 계약자적립금')),
                ('sign_charge7', models.DecimalField(decimal_places=2, default=6.06, max_digits=5, verbose_name='계약체결비용(7년 이내)')),
                ('sign_charge810', models.DecimalField(decimal_places=2, default=6.06, max_digits=5, verbose_name='계약체결비용(8년~10년)')),
                ('management_charge7', models.DecimalField(decimal_places=2, default=5.0, max_digits=7, verbose_name='관리/유지비용(7년 이내)')),
                ('management_charge810', models.DecimalField(decimal_places=2, default=3.23, max_digits=7, verbose_name='관리/유지비용(7년~10년)')),
                ('management_charge11', models.DecimalField(decimal_places=1, default=1.5, max_digits=5, verbose_name='관리/유지비용(10년 초과)')),
                ('sign_charge1', models.DecimalField(decimal_places=2, default=6.0, max_digits=5, verbose_name='계약체결비용(거치식)')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
    ]
