from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from .. import models
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from mypro.settings import BASE_DIR

import os


def cart_index(request):
    cartslist = models.Cart.objects.all()

    # 
    # # ======================  分页  ====================
    # paginator = Paginator(cartslist, 10)
    # # 获取请求的页数
    # p = int(request.GET.get('p', 1)
    # # 获取请求页的数据
    # cartslist = paginator.page(p)

    context = {'cartslist': cartslist}
    return render(request, 'myadmin/carts/index.html', context)
