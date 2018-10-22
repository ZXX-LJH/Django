from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from myadmin import models
from django.core.urlresolvers import reverse
from mypro.settings import BASE_DIR
import os


# 后台首页
def index(request):
    return render(request, 'myhome/index.html')

def list(request):
    return render(request, 'myhome/list.html')

def login(request):
    return render(request, 'myhome/login.html')

def cart(request):
    return render(request, 'myhome/cart.html')

def meilanx(request):
    return render(request, 'myhome/meilanx.html')

def order(request):
    return render(request, 'myhome/order.html')

def myorder(request):
    return render(request, 'myhome/myorder.html')

def register(request):
    return render(request, 'myhome/register.html')

def phone_check(request):
    phone1 = request.GET.get('phone1')
    num = models.Users.objects.get(phone = phone1)
    print(num.phone)
    # num = 1
    if num:
        return JsonResponse({'error':1,'msg':'手机号码已被注册'})
    else:
        return JsonResponse({'error':0,'msg':'手机号码未被注册'})



    return HttpResponse('phone_check')

def member(request):
    return render(request, 'myhome/member.html')
