# Generated by Django 2.0.13 on 2019-06-12 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20190612_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_percent',
            field=models.IntegerField(null=True),
        ),
    ]
