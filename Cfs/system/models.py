from django.db import models
from system.models import *

# Create your models here.
# 用户表：
#     个人ID
#     用户名
#     账号
#     密码
#     性别
#     手机号
#     用户权限标识
#
# 店铺表：
#     店铺ID
#     店铺名
#     店铺描述
#     店铺综合评分
#     店铺电话
#     菜单索引
#
# 菜单：
#     菜序列号
#     菜单名
#     菜单评分
#     菜价格
#     评论表ID
#
# 评论表：
#     评论表ID
#     用户ID
#     店铺ID
#     菜序列号
#     评分ID
#     评论信息
#
# 评论-用户：一个人只能发一条评论，所以 一对一的关系
# 评论-店铺：一个店铺可以有多条评论，所以 多对一的关系
# 评论-菜： 一个菜可以有多条评论，所以 多对一的关系
# 菜单-店铺：一个店铺可以有多个菜，所以 多对一的关系

# 用户表
class Users(models.Model):
    class Meta:
        db_table = 'sys_users'

    # 用户名
    user_name = models.CharField(null=False, unique=True, max_length=10)
    # 账号
    user_account = models.CharField(null=False, unique=True, max_length=10)
    # 密码
    user_password = models.CharField(null=False, max_length=15)
    # 绑定的角色表
    user_roles = models.OneToOneField(to='Roles', on_delete=models.CASCADE, null=False)

# 角色表
class Roles(models.Model):
    class Meta:
        db_table = 'sys_roles'
    # 用户年龄
    role_age = models.IntegerField(null=True)
    # 用户性别
    role_gender = models.CharField(max_length=1, null=True)
    # 用户手机号
    role_phone_number = models.IntegerField(null=True)

    # 用户店铺
    role_shop = models.ForeignKey(to='Shops',db_column="role_shop_id", on_delete=models.DO_NOTHING, null=True)
    # 用户菜单
    role_menus = models.ManyToManyField(to='Menus', db_column="role_menus_id" , null=False, db_table='sys_role_menus')
    # 用户权限
    role_permissions = models.ManyToManyField(to='Permissions',db_column="role_permissions_id" , db_table='sys_role_permissions')

# 菜单表
class Menus(models.Model):
    class Meta:
        db_table = 'sys_menus'

    # 菜单名称
    menu_name = models.CharField(null=False, unique=False, max_length=10)
    # 菜单的URL
    url = models.CharField(null=True, unique=False, max_length=255)
    # 菜单的URL的name
    url_name = models.CharField(null=True, unique=False, max_length=255)

    # 上一个菜单的ID
    menu_id = models.ForeignKey(to="Menus", db_column="menu_parent", related_name="children" ,on_delete=models.DO_NOTHING , null=True)


# 权限表
class Permissions(models.Model):
    class Meta:
        db_table = 'sys_permissions'

    # 显示名称
    display_name = models.CharField(null=False, unique=False, max_length=255)
    # url
    url_name = models.CharField(null=True, unique=True, max_length=255)

    # 用户权限
    menu = models.ForeignKey(to="Menus", db_column="menu_id", related_name="permissions", on_delete=models.DO_NOTHING, null=False)

# 店铺表
class Shops(models.Model):
    class Meta:
        db_table = 'sys_shops'

    # 店铺名
    shop_name = models.CharField(null=False, unique=True, max_length=20)
    # 店铺描述
    shop_description = models.TextField(null=False)
    # 店铺评分
    shop_overall_rating = models.IntegerField()
    # 店铺电话
    shop_phone_number = models.IntegerField()
    # 地铺地址

# 菜单表
class Cuisines(models.Model):
    class Meta:
        db_table = 'sys_cuisines'

    # 菜单名
    menu_name = models.CharField(null=False, unique=True, max_length=10)
    # 菜单评分
    menu_overall_rating = models.IntegerField()
    # 菜单价格
    menu_price = models.IntegerField()
    # 菜单-店铺：一个店铺可以有多个菜，所以 多对一的关系
    menu_shop = models.ForeignKey(to="Shops", db_column='menu_shop_id', on_delete=models.DO_NOTHING, null=False)

# 评论表
class Comments(models.Model):
    class Meta:
        db_table = 'sys_comments'

    # 评论信息
    comment_text = models.TextField(null=False, unique=True)
    # 评分
    comment_score = models.IntegerField(null=False, unique=True)
    # 评论-用户：一个人只能发一条评论，所以 一对一的关系
    comment_user = models.OneToOneField(to="Users", db_column="comment_user_id", on_delete=models.DO_NOTHING, unique=True)
    # 评论-店铺：一个店铺可以有多条评论，所以 多对一的关系
    comment_shop = models.ForeignKey(to="Shops", db_column="comment_shop_id", on_delete=models.DO_NOTHING, null=True)
    # 评论-菜： 一个菜可以有多条评论，所以 多对一的关系
    comment_menu = models.ForeignKey(to="Cuisines", db_column="comment_menu_id", on_delete=models.DO_NOTHING, )
