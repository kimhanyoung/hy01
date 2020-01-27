# Generated by Django 2.0.13 on 2019-04-29 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0010_auto_20190429_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='fund_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='meta_description',
            new_name='manage_company',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateField(default='2010-10-02', null=True, verbose_name='설정일'),
        ),
        migrations.AddField(
            model_name='product',
            name='fund_code',
            field=models.CharField(default='KLVL510000L', max_length=30, null=True, verbose_name='펀드유형'),
        ),
        migrations.AddField(
            model_name='product',
            name='fund_name02',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fund_type01',
            field=models.CharField(default='국내투자', max_length=30, null=True, verbose_name='펀드유형'),
        ),
        migrations.AddField(
            model_name='product',
            name='fund_type02',
            field=models.CharField(default='주식형', max_length=30, null=True, verbose_name='펀드유형'),
        ),
        migrations.AddField(
            model_name='product',
            name='input_percent',
            field=models.IntegerField(default=10, null=True, verbose_name='투입비율'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_percent',
            field=models.IntegerField(default=10, null=True, verbose_name='주식비중'),
        ),
    ]
