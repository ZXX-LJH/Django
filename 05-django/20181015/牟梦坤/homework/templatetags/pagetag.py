from django import template
register = template.Library()

# 自定义过滤器
@register.filter
def mmk_up(val):
    return val.upper()

# 自定义标签
from django.utils.html import format_html
@register.simple_tag
def jia(a,b):
    return int(a)+int(b)





