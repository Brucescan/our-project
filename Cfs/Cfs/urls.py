from django.contrib import admin
from django.urls import path,include
from Cfs import views

urlpatterns = [
    # 项目的根目录
    path("", views.index, name='index'),
    path("welcome.html", views.welcome, name='welcome'),
    # 子路由
    path("system", include('system.urls'))
]
