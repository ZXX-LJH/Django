from django.contrib import admin

# Register your models here.

from . models import VipUser


# Register your models here.
class VipUserAdmin(admin.ModelAdmin):
  # 要展示的字段
  list_display = ('id','username','email','phone','age','sex','addtime')

  #list_per_page设置每页显示多少条记录，默认是100条
  list_per_page = 10

  #ordering设置默认排序字段，负号表示降序排序
  ordering = ('id',)

  #list_editable 设置默认可编辑字段
  list_editable = ['username', 'age']

  #过滤器
  list_filter =('username', 'age', 'email') 

   #搜索字段
  search_fields =('username', 'age', 'email','phone') 
  
  date_hierarchy = 'addtime'    # 详细时间分层筛选　



admin.site.register(VipUser,VipUserAdmin)