from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404,JsonResponse
from django.core.urlresolvers import reverse

from . models import VipUser,UserInfo,Types,Goods,Books,Tags,Citys

# 定义视图函数
def index(request):

    # 响应文本信息
    # return HttpResponse('<h1 style="color:red">hello world</h1>')
    return render(request,'index.html')

# 加载 城市联动的页面
def city(request):
    
    # 获取一级城市信息
    data = Citys.objects.filter(level=1)

    return render(request,'city.html',{'citys':data})

def getcitys(request):
    # 获取请求的id参数
    upid = request.GET.get('id')

    # values()：一个对象构成一个字典，然后构成一个列表返回
    data = Citys.objects.filter(upid=upid).values()

    # [object,object,object]

    # [{},{},{}]

    return JsonResponse(list(data),safe=False)





# 验证码
def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # str1 = '123456789'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('FreeMono.ttf', 23)
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    #内存文件操作
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
