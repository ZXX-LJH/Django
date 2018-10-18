from django.conf.urls import url
from . import views

urlpatterns = [
    #首页
    url(r'^$', views.index,name='myhome_index'),
    # 会员添加



]