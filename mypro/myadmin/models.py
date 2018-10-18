from django.db import models

# Create your models here.
class Users(models.Model):
    # 用户名 密码  手机号 邮箱 性别 年龄 头像 注册时间  状态
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=77)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=100,null=True)
    sex = models.CharField(max_length=1,choices=((1,'男'),(0,'女')),null=True)
    age = models.IntegerField(null=True)
    pic_url = models.CharField(max_length=100,null=True)
    # 0 正常  1禁用
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)

