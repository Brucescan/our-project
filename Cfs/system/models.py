from django.db import models

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
        db_table = 'db_users'

    # 用户名
    user_name = models.CharField(null=False, unique=True, max_length=10)
    # 账号
    user_account = models.CharField(null=False, unique=True, max_length=10)
    # 密码
    user_password = models.CharField(null=False, max_length=15)
    # 性别
    user_gender = models.CharField(max_length=1)
    # 手机号
    user_phone_number = models.IntegerField()
    # 用户权限标识
    user_permissions = models.IntegerField(null=False)
    # 绑定的店铺
    user_shop = models.ForeignKey(to='Shops', on_delete=models.DO_NOTHING, null=True)


# 店铺表
class Shops(models.Model):
    class Meta:
        db_table = 'db_shops'

    # 店铺名
    shop_name = models.CharField(null=False, unique=True, max_length=20)
    # 店铺描述
    shop_description = models.TextField(null=False)
    # 店铺评分
    shop_overall_rating = models.IntegerField(max_length=2)
    # 店铺电话
    shop_phone_number = models.IntegerField()
    # 地铺地址

# 菜单表
class Menus(models.Model):
    class Meta:
        db_table = 'db_menus'

    # 菜单名
    menu_name = models.CharField(null=False, unique=True, max_length=10)
    # 菜单评分
    menu_overall_rating = models.IntegerField(max_length=2)
    # 菜单价格
    menu_price = models.IntegerField()
    # 菜单-店铺：一个店铺可以有多个菜，所以 多对一的关系
    menu_shop = models.ForeignKey(to="Shops", db_column='menu_shop_id', on_delete=models.DO_NOTHING,unique=True, null=False)

# 评论表
class Comments(models.Model):
    class Meta:
        db_table = 'db_comments'

    # 评论信息
    comment_text = models.TextField(null=False, unique=True)
    # 评分
    comment_score = models.IntegerField(null=False, unique=True)
    # 评论-用户：一个人只能发一条评论，所以 一对一的关系
    comment_user = models.OneToOneField(to="Users", db_column="comment_user_id", on_delete=models.DO_NOTHING, unique=True)
    # 评论-店铺：一个店铺可以有多条评论，所以 多对一的关系
    comment_shop = models.ForeignKey(to="Shops", db_column="comment_shop_id", on_delete=models.DO_NOTHING, null=True)
    # 评论-菜： 一个菜可以有多条评论，所以 多对一的关系
    comment_menu = models.ForeignKey(to="Menus", db_column="comment_menu_id", on_delete=models.DO_NOTHING, )
