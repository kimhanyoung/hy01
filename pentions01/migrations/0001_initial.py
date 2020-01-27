# Generated by Django 2.0.13 on 2020-01-12 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ma1000In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, help_text='5,7,10,12,15,10년납 중 선택', verbose_name='납입기간')),
                ('earning_rate', models.DecimalField(decimal_places=2, default=7.0, max_digits=5, verbose_name='수익률')),
                ('chulsu_start_year', models.IntegerField(default=10, verbose_name='철수시작')),
                ('result_year', models.IntegerField(default=30, verbose_name='결과보기')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma1000Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('earning_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='수익률')),
                ('chulsu_start_year', models.IntegerField(default=10, verbose_name='철수시작')),
                ('result_year', models.IntegerField(default=30, verbose_name='결과보기')),
                ('year', models.IntegerField()),
                ('younghee_total_premium', models.IntegerField()),
                ('chulsu_total_premium', models.IntegerField()),
                ('chulsu_surrender_value', models.IntegerField()),
                ('younghee_surrender_value', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma1000Out02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('younghee_total_premium', models.IntegerField()),
                ('younghee_surrender_value', models.IntegerField()),
                ('younghee_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='영희수익률')),
                ('chulsu_total_premium', models.IntegerField()),
                ('chulsu_surrender_value', models.IntegerField()),
                ('chulsu_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='영희수익률')),
                ('gap', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma2000In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('younghee_earning_rate', models.DecimalField(decimal_places=2, default=10, max_digits=5, verbose_name='수익률')),
                ('chulsu_earning_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='수익률')),
                ('result_year', models.IntegerField(default=30, verbose_name='결과보기')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma2000Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('younghee_earning_rate', models.DecimalField(decimal_places=2, default=10, max_digits=5, verbose_name='수익률')),
                ('chulsu_earning_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='수익률')),
                ('result_year', models.IntegerField(default=30, verbose_name='결과보기')),
                ('year', models.IntegerField()),
                ('total_premium', models.IntegerField()),
                ('chulsu_surrender_value', models.IntegerField()),
                ('younghee_surrender_value', models.IntegerField()),
                ('difference', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma2000Out02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_premium', models.IntegerField()),
                ('younghee_surrender_value', models.IntegerField()),
                ('younghee_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='영희수익률')),
                ('chulsu_surrender_value', models.IntegerField()),
                ('chulsu_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='영희수익률')),
                ('gap', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma3000In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('younghee_earning_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='수익률')),
                ('chulsu_earning_rate', models.DecimalField(decimal_places=2, default=5, max_digits=5, verbose_name='수익률')),
                ('result_year', models.IntegerField(default=30, verbose_name='결과보기')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ma3000Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.IntegerField(default=1000000, verbose_name='월보험료')),
                ('paying_period', models.IntegerField(default=10, verbose_name='납입기간')),
                ('younghee_earning_rate', models.DecimalField(decimal_places=2, default=7, max_digits=5, verbose_name='수익률')),
                ('chulsu_earning_rate', models.DecimalField(decimal_places=2, default=5, max_digits=5, verbose_name='수익률')),
                ('result_year', models.IntegerField(default=30, verbose_name='결과보기')),
                ('year', models.IntegerField()),
                ('total_premium', models.IntegerField()),
                ('chulsu_surrender_value', models.IntegerField()),
                ('chulsu_tax', models.IntegerField()),
                ('chulsu_tax_after', models.IntegerField()),
                ('younghee_surrender_value', models.IntegerField()),
                ('younghee_tax', models.IntegerField()),
                ('younghee_tax_after', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
