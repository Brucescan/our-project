from django.contrib import admin
from django.urls import path,include
from Cfs import views

urlpatterns = [
    # 项目的根目录
    path('', views.index)
]
