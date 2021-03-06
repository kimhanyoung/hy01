# Generated by Django 2.0.13 on 2019-12-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders03', '0016_af14graph_zero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ag00Fundalarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2005-01-05', verbose_name='날자')),
                ('fund_type', models.CharField(default='주식형유지', max_length=10, verbose_name='편드타입')),
                ('content', models.TextField(default='종합주가', verbose_name='내용')),
            ],
        ),
        migrations.AlterField(
            model_name='af01input',
            name='path_month',
            field=models.IntegerField(default=15, verbose_name='경과년'),
        ),
    ]
