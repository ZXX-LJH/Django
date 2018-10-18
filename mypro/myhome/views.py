from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from . import models
from django.core.urlresolvers import reverse
from mypro.settings import BASE_DIR
import os


# 后台首页
def index(request):
    return render(request, 'myhome/index.html')