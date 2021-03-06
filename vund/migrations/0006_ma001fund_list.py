# Generated by Django 2.2 on 2019-04-10 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vund', '0005_auto_20190410_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ma001fund_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_code', models.CharField(default='1234', max_length=30, verbose_name='펀드코드')),
                ('stock_percent', models.IntegerField(default=10, verbose_name='주식비중')),
                ('fund_name', models.CharField(default='주식형', max_length=30, verbose_name='펀드명')),
                ('fund_type01', models.CharField(default='주식형', max_length=30, verbose_name='펀드유형')),
                ('fund_type02', models.CharField(default='주식형', max_length=30, verbose_name='펀드유형')),
                ('input_percent', models.IntegerField(default=10, verbose_name='투입비율')),
                ('insu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vund.Ma000insu_list')),
            ],
        ),
    ]
