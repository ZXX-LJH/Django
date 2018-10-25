from django.conf.urls import url
from . import views

urlpatterns = [
    #首页
    url(r'^index/$', views.index,name='myhome_index'),
    # 列表
    url(r'^list/$', views.list,name='myhome_list'),
    url(r'^login/$', views.login,name='myhome_login'),
    url(r'^cart/$', views.cart,name='myhome_cart'),
    url(r'^meilanx/$', views.meilanx,name='myhome_meilanx'),
    url(r'^cartadd/$', views.cartadd,name='myhome_cartadd'),
    
    url(r'^order/$', views.order,name='myhome_order'),
    url(r'^myorder/$', views.myorder,name='myhome_myorder'),
    url(r'^countprice/$', views.countprice,name='myhome_countprice'),

    url(r'^register/$', views.register,name='myhome_register'),
    url(r'^phonecheck/$', views.phone_check,name='myhome_phone_check'),
    url(r'^memeber/$', views.member,name='myhome_member'),


]
