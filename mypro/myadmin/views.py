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
    return render(request, 'myadmin/index.html')

def user_index(request):
    data = models.Users.objects.all()
    context = {'userlist':data}

    return render(request, 'myadmin/user/index.html',context)


def user_add(request):
    return render(request, 'myadmin/user/add.html')

def user_register(request):

    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    print(data)
    # 密码加密
    # 对密码进行加密操作
    data['password'] = make_password(data['password'], None, 'pbkdf2_sha256')

    # 处理头像
    myfile = request.FILES.get('pic_url')
    if myfile:
        # 调用函数进行头像上传
        data['pic_url'] = uploads(myfile)
    else:
        data['pic_url'] = '/static/pics/user.jpg'

    # 执行数据的更新
    ob = models.Users(**data)
    ob.save()

    print('123412')
    data = models.Users.objects.all()
    context = {'userlist': data}
    return render(request,'myadmin/user/index.html', context )


# 封装函数进行文件上传
def uploads(myfile):
    import time

    # myfile.name  2.jpg  jpg
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open(BASE_DIR + "/static/pics/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    return "/static/pics/" + filename

def user_edit(request, uid):

    data = models.Users.objects.get(id=uid)
    context = {'uinfo': data}
    print(context)
    return render(request,'myadmin/user/edit.html',context)


def user_index_edit(request, uid):
    # 获取提交的数据
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')

    # 数据库获取对象
    user = models.Users.objects.get(id = uid)

    user.username = data['username']
    # 手机加密
    user.password = make_password(data['password'], None, 'pbkdf2_sha256')
    user.phone = data['phone']
    user.email = data['email']
    user.age = data['age']
    user.sex = data['sex']

    # 头像
    myfile = request.FILES.get('pic_url')
    if myfile:
        # 如果修改了头像,要上传新的头像,并判断是否删除以前头像
        if user.pic_url != '/static/pics/user.jpg':
            # 删除原来上传的头像
            os.remove(BASE_DIR + user.pic_url)

        # 更新头像
        user.pic_url = uploads(myfile)

    user.save()


    data = models.Users.objects.all()
    context = {'userlist': data}
    return render(request, 'myadmin/user/index.html', context)



def user_delete(request, uid):
    data = models.Users.objects.get(id = uid)
    data.delete()

    data = models.Users.objects.all()
    context = {'userlist': data}
    return render(request, 'myadmin/user/index.html', context)













