from django.shortcuts import render


# 整个项目的视图的根
# 欢迎页
def welcome(req):
    return render(req, 'welcome.html')


# 进入首页
def index(req):
    return render(req, 'index.html')


# 用户登录


# 退出登录
