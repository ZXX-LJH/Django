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
    #首页
    url(r'^$', views.index,name='myadmin_index'),

    # 会员添加
    url(r'^user/index/$', views.user_index, name='myadmin_user_index'),
    url(r'^user/index_edit/([0-9]+)/$', views.user_index_edit, name='myadmin_user_indexToedit'),

    url(r'^user/add/$', views.user_add, name='myadmin_user_add'),
    url(r'^user/register/$', views.user_register, name='myadmin_user_register'),
    url(r'^user/edit/(?P<uid>[0-9]+)/$', views.user_edit, name='myadmin_user_edit'),
    url(r'^user/delete/(?P<uid>[0-9]+)/$', views.user_delete, name='myadmin_user_delete'),

]