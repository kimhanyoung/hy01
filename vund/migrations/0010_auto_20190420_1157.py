# Generated by Django 2.0.13 on 2019-04-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vund', '0009_ma001fund_list_insu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ma001fund_list',
            name='insu_name',
            field=models.CharField(max_length=30, verbose_name='보험명'),
        ),
    ]
