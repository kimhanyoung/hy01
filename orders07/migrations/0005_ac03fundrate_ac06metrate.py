# Generated by Django 2.0.13 on 2019-11-06 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders07', '0004_auto_20191106_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ac03Fundrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_name', models.CharField(db_index=True, max_length=200)),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 기준가')),
                ('present_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 기준가')),
                ('fund_money', models.IntegerField(default=10000000, verbose_name='펀드 평가금액')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ac06Metrate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fund_name', models.CharField(db_index=True, max_length=200)),
                ('entry_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='가입시 기준가')),
                ('present_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='현재 기준가')),
                ('fund_money', models.IntegerField(default=10000000, verbose_name='펀드 평가금액')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='수익률')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
