from django.db import models

# Create your models here.
class VipUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    # 添加时间
    addtime = models.DateTimeField(auto_now_add=True)



class UserInfo(models.Model):
    # 第一个参数：是被关联的模型名称
    # 第二个参数：当user用户表中的一条数据被删除的时候，与之对应的详情表数据也会被删除
    uid = models.OneToOneField(VipUser, on_delete=models.CASCADE)
    xueli = models.CharField(max_length=10)
    yuanxiao = models.CharField(max_length=20)
    jiguan = models.CharField(max_length=20)



# 商品分类
class Types(models.Model):
    name = models.CharField(max_length=10)


# 商品
class Goods(models.Model):
    tid = models.ForeignKey(to="Types", to_field="id")
    title = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.title



# 书
class Books(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# 标签
class Tags(models.Model):
    name = models.CharField(max_length=10)
    bid = models.ManyToManyField(to="Books")

    def __str__(self):
        return self.name


# 城市模型
class Citys(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    upid = models.IntegerField()

    class Meta:
        db_table = 'citys'



