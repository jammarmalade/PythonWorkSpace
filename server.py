#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WSGI接口  Web Server Gateway Interface
# server.py 负责启动WSGI服务器 加载application()函数
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数， hello 为文件名，application为函数名
from hello import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 启动后，浏览器访问 http://127.0.0.1:8000/ 

'''


'''