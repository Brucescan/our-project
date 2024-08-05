from django.shortcuts import render


# 整个项目的视图的根
# 进入首页
def index(req):
    return render(req, 'index.html')
# 登录页
# 用户登录
# 退出登录
