# Generated by Django 2.0.13 on 2019-04-29 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_auto_20190423_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['insu_name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='meta_description',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='insu_name',
        ),
        migrations.AddField(
            model_name='category',
            name='insu_name02',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='sell_end',
            field=models.DateField(default='2099-12-31', null=True, verbose_name='판매종료'),
        ),
        migrations.AddField(
            model_name='category',
            name='sell_start',
            field=models.DateField(default='2010-10-02', null=True, verbose_name='판매개시'),
        ),
    ]
