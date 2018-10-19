from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from .. import models
from django.core.urlresolvers import reverse
from mypro.settings import BASE_DIR

import os


# 后台首页
def index(request):
    return render(request, 'myadmin/index.html')

def user_index(request):
    from django.core.paginator import Paginator
    # 获取所有数据
    data = models.Users.objects.all()
    print('data: ', data)

    # 数据不存在
    # if data == None:  # 返回的是空的查询集 但不为 None
    if len(data) == 0:
        return HttpResponse('<script>alert("数据库中未有数据,去注册");location.href="' + reverse('myadmin_user_add') + '"</script>')

    # ==================  搜索  ============================
    types = request.GET.get('types',None)
    keywords = request.GET.get('keyword',None)
    print(types)
    print(keywords)
    if types:
        if types == 'all':
            from django.db.models import Q
            data = data.filter(Q(username__contains=keywords)|Q(phone__contains=keywords)|Q(email__contains=keywords)|Q(age__contains=keywords))
        elif types == 'state':
            # keywords == 禁用
            arr = {'正常': 0, '禁用': 1, '删除': 3}
            data = data.filter(status=arr[keywords])
        else:
            # data = data.filter(username__contains=keywords)
            search = {types + '__contains': keywords}
            data = data.filter(**search)

    # ====================  分页  ==========================

    # 实例化分页类        (需要分页的数据   , 每页显示的数据)
    paginator = Paginator(data, 10)
    # 获取请求的页数
    p = request.GET.get('p',1)
    # 获取请求页的数据
    userlist = paginator.page(p)

    # print(userlist)  # <Page 3 of 7>
    # print(data)
    # print(paginator.page_range)  # range(1, 8)

    return render(request, 'myadmin/user/index.html',{'userlist':userlist})

# 注册  >> 加载注册页面
def user_add(request):
    return render(request, 'myadmin/user/add.html')

# 注册 >> 将注册页的数据  交由 后台保存
def user_register(request):
    # 获取注册页的表单书数据   POST方式提交的  多了一个 csrf数据
    data = request.POST.dict()
    # 弹出 csrf 数据   不用可不弹出
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

    # 执行数据的更新  先获取对象在执行操作
    ob = models.Users(**data)
    ob.save()

    # 这种传递数据会影响后面  分页功能
    # data = models.Users.objects.all()
    # context = {'userlist': data}
    # return render(request,'myadmin/user/index.html', context )

    return HttpResponse('<script>alert("添加成功");location.href="' + reverse('myadmin_user_index') + '"</script>')

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

# 修改 (获取后台数据 --> 到edit.html渲染
def user_edit(request, uid):
    data = models.Users.objects.get(id=uid)
    context = {'uinfo': data}
    # print(context)
    return render(request,'myadmin/user/edit.html',context)

# 修改 >> 接收 edit 提交的数据交由后台进行更新
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
    return HttpResponse('<script>alert("修改成功");location.href="' + reverse('myadmin_user_index') + '"</script>')

#　删除　　　＞＞　物理删除　｜　逻辑删除
def user_delete(request, uid):
    data = models.Users.objects.get(id = uid)
    data.delete()

    # 这种传递数据会影响后面  分页功能
    # data = models.Users.objects.all()
    # context = {'userlist': data}
    # return render(request, 'myadmin/user/index.html', context)

    # 故采用以下这种方式
    return HttpResponse('<script>alert("删除成功");location.href="' + reverse('myadmin_user_index') + '"</script>')
