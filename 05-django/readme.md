复习:

    定义模型

    生成迁移文件

    执行迁移

    修改模型(添加字段,修改字段)

    生成迁移文件(注意:如果添加字段,则需要说明已有的数据,该字段如何处理,)

    执行迁移


    查询
        User.objects.all()
        User.objects.filter(username='zhangsan')
        User.objects.exclude(username='zhangsan')

        User.objetcs.get(id=1)
        User.objetcs.count()

    添加
        Users.objects.create(**{})

    删除
        ob.delete()

    修改
        ob.username = 'aa'
        ob.save()


    模型的关系
        一对一
            用户和用户详情,一个用户只有一个详情信息,一个详情信息也只对应一个用户
        一对多
            一个班级中有多个学员,多个学员在一个班级,
            一个商品分类下右多个商品,多个商品属于一个分类            
        多对多
            一本书有多个标签,标签下可以有多本书

    <!-- 会员管理再来一遍 -->



HttpReqeust对象
    请求对象



记录状态,http请求协议是无状态的协议,记不住用户的信息,因为需要借助一些服务来记住用户的一些状态

cookie
    是把数据存在的浏览器中,
    内容受限,key==>value 都是字符串
    容易被恶意获取,不能有效保护隐私

    用法:
        用响应对象进行设置
        res = HttpResponse()
        res.set_cookie()

        使用请求对象进行获取
        request.COOKIES.get()

session
    是在服务器端进行存储数据(数据库,文件,redis)
    内容丰富,key是字符串,值可以是任意类型
    他数据存储在服务器,不容易被获取,
    session在存储数据时会生成一个key(sessionid),把sessionid存储到浏览器的cookie中
    每一次请求,都用cookie中sessionid去验证数据,


GET,POST 值的获取
    获取一键一值的时候
        http://127.0.0.1/user/list/?a=1&b=2&c=3
        如果是get方式传递
            request.GET['abc'] # 如果abc不存在会报错
            request.GET.get('abc',None) #如果abc不存在则读取默认值
        如果是post方式传递
            request.POST['abc'] # 如果abc不存在会报错
            request.POST.get('abc',None) #如果abc不存在则读取默认值

    获取一键多值
        http://127.0.0.1/user/list/?a=1&a=2&c=3
        request.GET.getlist('a',None)
        request.POST.getlist('a',None) # a=[1,2]



响应对象
    普通文本,加载模板,重定向,返回json
    data = [
        {'username':'zhangsan','age':21},
        {'username':'lisi','age':25},
        {'username':'wangwu','age':28},
        {'username':'zhaoliu','age':20},
    ]
    # 注意在使用JsonResponse响应json数据时,如果数据不是字典类型,则需要设置,safe=False
    return JsonResponse(data,safe=False)


验证码



ajax实例
	创建模型

	填充数据

	配置静态文件


	1,显示一个 城市联动的 html页面

	2,在html页面中 循环一级数据

	3,定义一个路由给 请求数据使用

	4,在视图函数中 接收id获取下一级的数据,并返回json格式

	5,在html的页面中 绑定事件,获取id.发送ajax请求

	6,在ajax中判断是否有返回数据,
		如果有返回数据,则动态创建下拉选框,添加数据

	注意:
		最后一级没有数据,但是创建选框,(解决:在返回数据时判断)

		每次选择元素都创建新的,不会删除原来的选框
		解决:当选中元素时,移出当前元素之后的所有元素

作业:
	笔记
	练习:
		session操作 2遍

		城市联动的实例 2遍 要求能默写




模板


git版本控制器


项目开发流程


项目审核标准



