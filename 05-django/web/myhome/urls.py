"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    # 参数1  路由规则   参数2,指定的视图函数
    url(r'^$', views.index),

    url(r'^vi/$', views.vi),

    # 请求对象
    url(r'^req/$', views.req),

    # cookie 设置
    url(r'^setcok/$', views.setcok),
    url(r'^getcok/$', views.getcok),

    # 设置 session
    url(r'^setsess/$', views.setsess),
    # 获取
    url(r'^getsess/$', views.getsess),
    # 删除
    url(r'^outsess/$', views.outsess),

    # 响应对象
    url(r'^resp/$', views.resp),

    # 验证码
    url(r'^verifycode/$',views.verifycode),

    # 显示 城市联动的页面
    url(r'^city/$',views.city),
    url(r'^getcitys/$',views.getcitys,name="getcitys"),


]
