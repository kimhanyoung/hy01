# Generated by Django 2.0.13 on 2019-04-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20190429_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manage_company',
            field=models.TextField(blank=True, null=True),
        ),
    ]
