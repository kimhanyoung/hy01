# Generated by Django 2.0.13 on 2019-04-29 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20190429_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['fund_name']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_display',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_order',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]
