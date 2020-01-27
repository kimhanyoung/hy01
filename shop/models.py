from django.db import models
from django.contrib.auth.models import User
import datetime

from django.urls import reverse

class Category(models.Model):
    insu_name = models.CharField(max_length=200, db_index=True)
    insu_name02 = models.CharField(max_length=200, db_index=True, null=True )
    company = models.TextField(blank=True)
    sell_start = models.DateField('판매개시', default='2010-10-02',null=True)
    sell_end = models.DateField('판매종료', default='2099-12-31',null=True)

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['insu_name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.insu_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    insu_name = models.CharField(max_length=200, db_index=True, null=True)
    fund_name = models.CharField(max_length=200, db_index=True)
    fund_name02 = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    fund_code = models.CharField('펀드유형', max_length=30, default='KLVL510000L', null=True)
    fund_type01 = models.CharField('펀드유형', max_length=30, default='국내투자', null=True)
    fund_type02 = models.CharField('펀드유형', max_length=30, default='주식형', null=True)
    stock_percent = models.IntegerField(null=True)

    manage_company = models.TextField(blank=True, null=True)
    create_date = models.DateField('설정일', default='2010-10-02', null=True)

    price = models.IntegerField(null=True)


    class Meta:
        ordering = ['fund_name']
        index_together = [['id','slug']]

    def __str__(self):
        return self.fund_name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



