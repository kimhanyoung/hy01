# Generated by Django 2.0.13 on 2019-04-22 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vund', '0013_auto_20190422_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ma001fund_list',
            name='stock_percent',
        ),
    ]
