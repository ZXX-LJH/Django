from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from myadmin import models
from django.core.urlresolvers import reverse
from mypro.settings import BASE_DIR
from django.contrib.auth.hashers import make_password, check_password
import os


# 后台首页
def index(request):
    # 获取所有的以及分类
    data = models.Cates.objects.filter(pid = 0)

    # 获取当前以及分类下的所有二级分类
    for i in data:
        i.sub = models.Cates.objects.filter(pid = i.id)

    context = {'data': data}

    return render(request, 'myhome/index.html', context)

def list(request):
    return render(request, 'myhome/list.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'myhome/login.html')
    elif request.method == 'POST':
        # print(request.POST['verifycode'])
        # print(request.session['verifycode'])
        if request.POST['verifycode'] == request.session['verifycode']:
            phone = request.POST['phone']
            user = models.Users.objects.get(phone = phone)
            mark = check_password(request.POST['password'],user.password)
            if mark:
                # 用户和密码都输入正确
                # 在session 中存入登录凭证
                request.session['VipUser'] = {'username':user.username, 'phone':user.phone, 'uid':user.id,'pic_url': user.pic_url}
                # print(request.session['VipUser'])
                # print(request.session['VipUser']['pic_url'])
                return HttpResponse('<script>alert("登录成功");location.href="' + reverse('myhome_index') + '"</script>')
            else:
                return HttpResponse('<script>alert("密码不正确，请重新登录");location.href="' + reverse('myhome_login') + '"</script>')
        else:
            return HttpResponse('<script>alert("验证码错误");location.href="' + reverse('myhome_login') + '"</script>')
    # return HttpResponse('login')

def cart(request):
    return render(request, 'myhome/cart.html')

def meilanx(request):
    return render(request, 'myhome/meilanx.html')

def order(request):
    return render(request, 'myhome/order.html')

def myorder(request):
    return render(request, 'myhome/myorder.html')

def register(request):

    if request.method == 'GET':
        return render(request, 'myhome/register.html')
    elif request.method == 'POST':
        # 判断手机号是否已存在
        try:
            # 冒错则说明不存在指定用户
            if models.Users.objects.get(phone = request.POST['phone']):
                return HttpResponse('<script>alert("手机号码已存在，请重新注册");location.href="' + reverse('myhome_register') + '"</script>')
        except:
        # 判断验证码是否正确
            if request.POST.get('verifycode') == request.session['verifycode']:
                # 获取表单提交的数据
                data = request.POST.dict()
                print(data)
                # 实例化会员类
                user = models.Users()
                user.username = 'user' + data['phone']
                user.password = make_password(data['password'], None, 'pbkdf2_sha256')
                user.phone = data['phone']
                # 写进数据库
                user.save()
                # 清楚session
                request.session['verifycode'] = ""
                return HttpResponse('<script>alert("注册成功");location.href="' + reverse('myhome_login') + '"</script>')
            else:
                return HttpResponse('<script>alert("验证码输入错误");location.href="' + reverse('myhome_register') + '"</script>')
def phone_check(request):
        phone = request.GET.get('phone')
        num = models.Users.objects.get(phone = phone)
        # print(num.phone)
        # num = 1
        if num:
            return JsonResponse({'error':1,'msg':'手机号码已被注册'})
        else:
            return JsonResponse({'error':0,'msg':'手机号码未被注册'})
    # return HttpResponse('phone_check')

def member(request):
    return render(request, 'myhome/member.html')
