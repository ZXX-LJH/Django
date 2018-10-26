from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from myadmin import models
from django.core.urlresolvers import reverse
from mypro.settings import BASE_DIR
from django.db.models import Q
from django.core.paginator import Paginator
import os


# 前台首页
def index(request):
    # 获取所有的以及分类
    data = models.Cates.objects.filter(pid = 0)

    # 获取当前以及分类下的所有二级分类
    for i in data:
        i.sub = models.Cates.objects.filter(pid = i.id)

    context = {'data': data}
    return render(request, 'myhome/index.html', context)
# 前台列表页
def list(request):
    cateid = request.GET.get('catetype') # 一级分类提交的数据
    goodid = request.GET.get('goodtype') # 二级分类提交的数据
    sortid = request.GET.get('sorttype') # 搜索分类提交的数据
    print(cateid)
    print(goodid)
    print(sortid)

    '''
    [
        'name':'点心/蛋糕',
            'sub':[
                'name':'点心','goodslist':[
                        goodsobject,goodsobject
                    ],
                'name':'蛋糕','goodslist':[
                        goodsobject,goodsobject
                    ]
                ],
        'name':'饼干/膨化','sub':['name':'饼干','goodslist':[goodsobject,goodsobject],'name':'膨化','goodslist':[goodsobject,goodsobject]]
    ]
    '''
    # 获取所有的商品信息
    data1 = models.Goods.objects.all()  # 所有商品
    # 获取所有的标签
    data2 = models.Cates.objects.filter(pid = 0)  #　所有一级标签
    for i in data2:
        i.sub = models.Cates.objects.filter(pid = i.id) # 一级标签下嵌套所有二级标签

    data3 = "" # 某一级标签下的所有子类标签
    listvar1 =[]
    if cateid == '0':  # 全部
        pass
    elif cateid:  # 如果点击了一级标签
        # 获取请求 cateid 的所有子标签
        data3 = models.Cates.objects.filter(pid = cateid)  # 传递给二级标签的数据
        for i in data3:
            for j in models.Goods.objects.filter(Q(cateid = i.id)):
                listvar1.append(j)
            # for i in len(listvar2):
            #     listvar1.append(i)
            # data1 = models.Goods.objects.filter(Q(cateid = i.id))
        data1 = listvar1  # 指定一级标签下的指定二级标签
        # print(listvar1)

    if goodid:  # 如果点击了二级标签
        data1 = models.Goods.objects.filter(cateid = goodid)  # 指定二级下的所有商品

    # ======================  搜索  ====================
    if sortid == 'index':
        pass
    elif sortid == 'new':
        data1 = models.Goods.objects.filter(status = 0)
    elif sortid == 'remai':
        data1 = models.Goods.objects.filter(status = 1)
    elif sortid == 'price':
        data1 = models.Goods.objects.filter(price__gt = 0).order_by('price')
        print('data1', data1)
        if cateid:
            for i in data3:
                print('data2', data1)
        if goodid:
            data1 = data1.filter(cateid = goodid)
            print('data3', data1)
    elif sortid == 'clicknum':
        data1 = models.Goods.objects.filter(clicknum__gt = 0).order_by(clicknum)
    elif sortid == 'ordernum':
        data1 = models.Goods.objects.filter(ordernum__gt = 0).order_by(ordernum)

    # ======================  分页  ====================
    paginator = Paginator(data1, 12)
    p = request.GET.get('p', 1)
    data1 = paginator.page(p)

    context = {'goodslist':data1,'cateslist_one':data2, 'cateslist_two':data3, 'cateid':cateid,"goodid":goodid, 'sortid':sortid}
    return render(request, 'myhome/list.html', context)
    return render(request, 'myhome/list.html')
# 登录页
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
    id = request.GET.get('id')
    # print('id = ', id , type(id))
    info = models.Goods.objects.filter(id = int(id))
    # print(info, type(info))
    context = {'goods': info,"id":id }
    return render(request, 'myhome/meilanx.html', context)

def cartadd(request):
    # 商品id  商品数量 用户id
    gid = request.GET.get('gid')
    num = int(request.GET.get('num'))
    uid = request.session['VipUser']['uid']

    goods = models.Goods.objects.get(id = gid)
    user = models.Users.objects.get(id = uid )

    # 检查当前的商品是否已经存在购物车
    res = models.Cart.objects.filter(uid = user).filter(goodsid = goods)
    if res.count():
        for i in res:  # 查询集  ==============  *** 有坑 *** =  =============
            i.num += num
            i.save()
        print(gid, '****************************')
    else:
        cart = models.Cart(goodsid = goods, uid = user, num = num)
        cart.save()
        print(num, '****************************')

    return JsonResponse({'error':0,'msg':'加入购物成功'})

def order(request):
    # 接收 cartids
    cartids = eval(request.GET.get('cartids'))  # 获得商品的编号  ['10', '8', '2', '3']
    nums = eval(request.GET.get('nums'))  # 商品的购买数量

    # 将cartids 中字符串转成 整形
    for i in range(0, len(cartids)):
        cartids[i] = int(cartids[i])
    # print(cartids)

    # 获取对应的购物车数据
    for i in cartids:
        good = models.Goods.objects.get(id = i) # 通过 商品编号获得 货物对象
        # 通过货物对象 修改 购物车中的数量
        cart = models.Cart.objects.get(goodsid = good)
        cart.num = int(nums[cartids.index(i)])
        cart.save()

    # 获得商品标号对应的对象
    data = models.Goods.objects.filter(id__in = cartids)
    print(data)
    # 分配数据
    context = {'data':data}

    return render(request,'myhome/order.html',context)


def myorder(request):
    # 如果用户登录了
    if request.session['VipUser']:
        # request.session['VipUser'] = {'username':user.username, 'phone':user.phone, 'uid':user.id,'pic_url': user.pic_url}
        # 通过用户手机号获得用户
        user = models.Users.objects.filter(phone = request.session['VipUser']['phone'])
        # print('user = ', user)
        # 通过用户获得购物车中的数据
        cart = models.Cart.objects.filter(uid = user)  # 外键  需要一个用户对象

        # 加载魔板
        context = {'cart': cart}
        # 返回数据
        return render(request, 'myhome/myorder.html', context)
# 计算购物的价格
def countprice(request):
    num = request.GET.get('num')
    id = request.GET.get('id')
    price = models.Goods.objects.get(id = int(id)).price
    res = price * int(num)
    return JsonResponse({'countprice':res})
# 注册用户
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
                user.username = 'user_' + data['phone']
                user.password = make_password(data['password'], None, 'pbkdf2_sha256')
                user.phone = data['phone']
                # 写进数据库
                user.save()
                # 清楚session
                request.session['verifycode'] = ""
                return HttpResponse('<script>alert("注册成功");location.href="' + reverse('myhome_login') + '"</script>')
            else:
                return HttpResponse('<script>alert("验证码输入错误");location.href="' + reverse('myhome_register') + '"</script>')
# 检查手机是否存在
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
