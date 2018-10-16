from django.conf.urls import url,include
from . import views

urlpatterns = [
    # 上传文件
    # 返回的上传文件的界面
    url(r'^fileform',views.fileform,name='fileform'),
    # 点击add之后,保存在本地,并返回一个提示信息
    url(r'^fileload',views.fileload,name='fileload'),

    # 模板
    url(r'^tmp',views.tmp,name='tmp'),

    # 视图函数的演示
    url(r'^viw',views.viw,name='viw'),
    url(r'^req/$',views.req,name='req'),
    url(r'^setcok',views.setcok,name='setcok'),
    url(r'^getcok',views.getcok,name='getcok'),
    url(r'^setses',views.setses,name='setses'),
    url(r'^getses',views.getses,name='getses')
]
