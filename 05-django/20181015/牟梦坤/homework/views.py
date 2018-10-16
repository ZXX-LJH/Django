from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse,JsonResponse
import time
from day4.settings import BASE_DIR
from django.core.urlresolvers import reverse

# Create your views here.

# 访问该网址返回添加上传文件的页面
def fileform(request):
    return render(request,'form.html')

# 定义保存文件到本地的函数
# myfile表示的一个操作对象
def uploads(myfile):
    # 为了同一文件多次上传成功并不重名,使用时间戳的方式给文件夹命名
    # enctype="multipart/form-data"是返回该上传文件的后缀名,并一并命名到新的文件夹上
    filename = str(time.time())+'.'+myfile.name.split('.').pop()
    # 打开文件夹,并保存上传文件
    # 使用wb+的方式(二进制流)创建一个空的且后缀与上传文件后缀一致的文件夹
    destination = open(BASE_DIR+'/uploads/'+filename,'wb+')
    # chunks表示的是将文件分块,分块的目的是提高上传速度
    for chunk in myfile.chunks():
        # 将每个分块依次存入到指定文件夹内
        destination.write(chunk)
    # 上传完成之后,关闭该文件夹
    destination.close()

def fileload(request):
    # 获取被上传的文件对象
    myfile = request.FILES.get('pic')
    # 如果选择了上传文件,则执行下列操作
    if myfile:
        uploads(myfile)
    # 完成上传之后返回提示信息
    return HttpResponse('ADD!')

def tmp(request):
    context = {'abc':'abc'}
    context['arr'] = ['a','b','c']
    context['nav'] = {'a':'a','b':'b'}
    context['shtml'] = '<h1 style="color:red;">i love you</h1>'
    return render(request,'tmp.html',context)

def viw(request):
    # 重定向,或者使用js(location.href)
    # return redirect(reverse('fileload'))
    context = {'u':reverse('fileload'),'msg':'success!'}
    return render(request,'info.html',context)

def req(request):
    # print(request.path)
    # print(request.method)
    # 有若干个则返回最后一个
    # print(request.GET.get('hobby'))
    # 有多少个就返回多少
    # print(request.GET.getlist('hobby'))
    #
    # print(request.GET.get('li',None))
    return HttpResponse('aa')

def setcok(request):
    res = HttpResponse('set cookie')
    res.set_cookie('uid',11)
    res.set_cookie('name','mmk')
    return res

def getcok(request):
    print(request.COOKIES.get('uid'))
    print(request.COOKIES.get('name'))
    return HttpResponse('getcookies')

def setses(request):
    request.session['vipuser'] = {'uid':1,'name':'mmk'}
    request.session['adminuser'] = 'abcd'
    return HttpResponse('setses')

def getses(request):

    # del request.session['adminuser']

    # print(request.session['vipuser'])
    # print(request.session['adminuser'])

    # request.session.clear()
    request.session['vipuser'] = {'uid': 1, 'name': 'mmk'}
    request.session.flush()
    return HttpResponse('getses')













