from django import template

register = template.Library()

@register.filter
def monthly_pention(value):
    return value/12

@register.filter            # 1
def cal(value):
    return value