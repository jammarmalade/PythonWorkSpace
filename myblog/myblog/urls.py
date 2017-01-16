"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
# 加入自己模块下的函数
from web import views as web_views

urlpatterns = [
    # 加入路由
    url(r'^$', web_views.index),
    # add 函数
    url(r'^add/', web_views.add, name='add'),
    # 优化的 url
    # url(r'^add2/(\d+)/(\d+)/$', web_views.add2, name='add2'),
    # 跳转 url
    url(r'^add2/(\d+)/(\d+)/$', web_views.redirect_add2),
    # 要与views.py中的函数大小对应，name 的作用: 主要用于生成 url,一旦定义不要轻易修改，便于以后优化 url 时不用到处改链接
    url(r'^getAddress/$', web_views.getAddress, name='getAddress'),
    url(r'^new_add/(\d+)/(\d+)/$', web_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
    # home 主页
    url(r'^home/', web_views.home, name='home'),
]
'''
为静态文件分配多个不同的网址时
import os
from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR,'media2')
    urlpatterns += static('/media2/', document_root=media_root)
'''