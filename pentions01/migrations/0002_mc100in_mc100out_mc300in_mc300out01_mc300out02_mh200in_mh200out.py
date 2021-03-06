# Generated by Django 2.0.13 on 2020-01-13 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pentions01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mc100In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life_expectancy', models.IntegerField(default=90, verbose_name='기대여명')),
                ('gender', models.CharField(default='남자', max_length=5, verbose_name='성별')),
                ('pention_start_rate', models.DecimalField(decimal_places=1, default=2.0, max_digits=3, verbose_name='연금개시시이율')),
                ('reserve_money', models.IntegerField(default=100000000, verbose_name='준비자금')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mc100Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('life_expectancy', models.IntegerField(default=90, null=True, verbose_name='기대여명')),
                ('gender', models.CharField(default='남자', max_length=5, null=True, verbose_name='성별')),
                ('pention_start_rate', models.DecimalField(decimal_places=1, default=2.0, max_digits=3, null=True, verbose_name='연금개시시이율')),
                ('present_age', models.IntegerField(default=45, null=True, verbose_name='현재연령')),
                ('reserve_money', models.IntegerField(default=100000000, null=True, verbose_name='준비자금')),
                ('wholelife_annuity_10', models.IntegerField(null=True)),
                ('wholelife_annuity_20', models.IntegerField(null=True)),
                ('wholelife_annuity_80', models.IntegerField(null=True)),
                ('annuity_certain_10', models.IntegerField(null=True)),
                ('annuity_certain_15', models.IntegerField(null=True)),
                ('annuity_certain_20', models.IntegerField(null=True)),
                ('annuity_inherit', models.IntegerField(null=True)),
                ('lump_sum_of_death', models.IntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mc300In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='남자', max_length=5, verbose_name='성별')),
                ('start_year', models.IntegerField(default=2010, verbose_name='납입년')),
                ('start_month', models.IntegerField(default=10, verbose_name='납입월')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('pention_start_age', models.IntegerField(default=65, verbose_name='연금개시연령')),
                ('earning_rate', models.DecimalField(decimal_places=1, default=7.0, max_digits=5, verbose_name='변액수익률')),
                ('first_pention_start_rate', models.DecimalField(decimal_places=1, default=5.0, max_digits=3, verbose_name='연금개시시이율')),
                ('second_pention_start_rate', models.DecimalField(decimal_places=1, default=2.0, max_digits=3, verbose_name='연금개시시이율')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mc300Out01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='남자', max_length=5, verbose_name='성별')),
                ('start_year', models.IntegerField(default=2010, verbose_name='납입년')),
                ('start_month', models.IntegerField(default=10, verbose_name='납입월')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('pention_start_age', models.IntegerField(default=65, verbose_name='연금개시연령')),
                ('earning_rate', models.DecimalField(decimal_places=1, default=7.0, max_digits=5, verbose_name='변액수익률')),
                ('first_pention_start_rate', models.DecimalField(decimal_places=1, default=5.0, max_digits=3, verbose_name='연금개시시이율')),
                ('second_pention_start_rate', models.DecimalField(decimal_places=1, default=2.0, max_digits=3, verbose_name='연금개시시이율')),
                ('first_wholelife_annuity_10', models.IntegerField()),
                ('first_wholelife_annuity_20', models.IntegerField()),
                ('first_wholelife_annuity_80', models.IntegerField()),
                ('first_annuity_certain_10', models.IntegerField()),
                ('first_annuity_certain_15', models.IntegerField()),
                ('first_annuity_certain_20', models.IntegerField()),
                ('first_annuity_inherit', models.IntegerField()),
                ('first_lump_sum_of_death', models.IntegerField()),
                ('reserve_money', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mc300Out02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_wholelife_annuity_10', models.IntegerField()),
                ('second_wholelife_annuity_20', models.IntegerField()),
                ('second_wholelife_annuity_80', models.IntegerField()),
                ('second_annuity_certain_10', models.IntegerField()),
                ('second_annuity_certain_15', models.IntegerField()),
                ('second_annuity_certain_20', models.IntegerField()),
                ('second_annuity_inherit', models.IntegerField()),
                ('second_lump_sum_of_death', models.IntegerField()),
                ('reserve_money', models.IntegerField()),
                ('life_table', models.CharField(default='8회', max_length=5, verbose_name='경험생명표')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mh200In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='남자', max_length=5, verbose_name='성별')),
                ('start_year', models.IntegerField(default=2010, verbose_name='납입년')),
                ('start_month', models.IntegerField(default=10, verbose_name='납입월')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('pention_start_age', models.IntegerField(default=65, verbose_name='연금개시연령')),
                ('a_earning_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='a원장 님수익률')),
                ('b_earning_rate', models.DecimalField(decimal_places=2, default=5, max_digits=5, verbose_name='b원장님 수익률')),
                ('pention_start_rate', models.DecimalField(decimal_places=1, default=2.0, max_digits=3, verbose_name='연금개시시이율')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mh200Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='남자', max_length=5, verbose_name='성별')),
                ('start_year', models.IntegerField(default=2010, verbose_name='납입년')),
                ('start_month', models.IntegerField(default=1, verbose_name='납입월')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('present_age', models.IntegerField(default=45, verbose_name='현재연령')),
                ('pention_start_age', models.IntegerField(default=65, verbose_name='연금개시연령')),
                ('a_earning_rate', models.DecimalField(decimal_places=2, default=7.0, max_digits=5, verbose_name='a원장 님수익률')),
                ('b_earning_rate', models.DecimalField(decimal_places=2, default=4.0, max_digits=5, verbose_name='b원장님 수익률')),
                ('pention_start_rate', models.DecimalField(decimal_places=1, default=2.0, max_digits=3, verbose_name='연금개시시이율')),
                ('a_wholelife_annuity_10', models.IntegerField()),
                ('a_wholelife_annuity_20', models.IntegerField()),
                ('a_wholelife_annuity_80', models.IntegerField()),
                ('a_annuity_certain_10', models.IntegerField()),
                ('a_annuity_certain_15', models.IntegerField()),
                ('a_annuity_certain_20', models.IntegerField()),
                ('a_annuity_inherit', models.IntegerField()),
                ('a_lump_sum_of_death', models.IntegerField()),
                ('b_wholelife_annuity_10', models.IntegerField()),
                ('b_wholelife_annuity_20', models.IntegerField()),
                ('b_wholelife_annuity_80', models.IntegerField()),
                ('b_annuity_certain_10', models.IntegerField()),
                ('b_annuity_certain_15', models.IntegerField()),
                ('b_annuity_certain_20', models.IntegerField()),
                ('b_annuity_inherit', models.IntegerField()),
                ('b_lump_sum_of_death', models.IntegerField()),
                ('total_premium', models.IntegerField()),
                ('b_reserve_money', models.IntegerField()),
                ('a_reserve_money', models.IntegerField()),
                ('life_table', models.CharField(default='8회', max_length=5, verbose_name='경험생명표')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
