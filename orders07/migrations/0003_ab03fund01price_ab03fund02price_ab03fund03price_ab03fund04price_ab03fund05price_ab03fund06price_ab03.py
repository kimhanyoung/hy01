# Generated by Django 2.0.13 on 2019-11-05 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders07', '0002_auto_20191104_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ab03fund01price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund02price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund03price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund04price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund05price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund06price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund07price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund08price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ab03fund09price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='일련번호')),
                ('fund_code', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(default='2010-10-02', null=True, verbose_name='기준일자')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='기준가')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
