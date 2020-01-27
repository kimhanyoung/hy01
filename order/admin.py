'''from django.contrib import admin

import csv
import datetime
from django.http import HttpResponse



from .models import OrderItem, Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','address','paid','created','updated']
    list_filter = ['paid','created','updated']
    inlines = [OrderItemInline] # 다른 모델과 연결되어있는 경우 한페이지 표시하고 싶을 때


admin.site.register(Order, OrderAdmin) '''