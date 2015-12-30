#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

'''
from urllib.parse import parse_qs
from html import escape
from urllib import request
from queue import Queue
import threading, time, re, json
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	d = parse_qs(environ['QUERY_STRING'])
	startPage = escape(d.get('p', [''])[0])
	if environ['PATH_INFO'][1:] !='get':
		exit()
	startPage = startPage if startPage!='' else 1
	endPage = int(startPage) + 5
	# 执行获取
	start = time.time()
	curl(startPage,endPage)
	end = time.time()
	body = '<h1>正在获取第 %s - %s 页数据</h1>' % (startPage,endPage)
	haoshi = '<h2>耗时 : %0.2f</h2>' % (end - start)
	body = body + haoshi
	if endPage < 10:
		body = body+'<br> 3 秒后将获取下一页<script language="javascript">setTimeout("location=\'http://127.0.0.1:8000/get?p='+str(endPage)+'\'",3000);</script>'

	return [body.encode('utf-8')]

q = Queue()
def curl(startPage,endPage):
	l = list(range(int(startPage), int(endPage)))
	for page in l:
		t = threading.Thread(target=doGet)
		# 主线程结束时，也把子线程杀掉
		t.setDaemon(True)
		t.start()
		# 放入队列
		q.put(page)
	# 等待所有队列中的所有任务完成
	q.join()

def doGet():
	while True:
		paged = q.get()
		rurl = 'http://bbs.csdn.net/forums/PHP?page=%d' % paged
		# 创建一个请求
		csdn = request.Request(rurl)
		# 添加 agent
		csdn.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
		with request.urlopen(csdn) as f:
			html = f.read().decode('utf-8')
			cachefile = './cache/csdn-%s.html' % paged
			fput = open(cachefile, 'w',encoding='utf-8')
			# 直接写入 html 
			# fput.write(html)
			# 正则匹配出内容后写入
			'''
			'''
			pattern = re.compile(r'<a\s*href="(\/topics\/\d+)"[^>]+?>(.+?)<\/a>')
			m = pattern.findall(html)
			list = []
			i=0
			for k,v in m:
				str = '<a href="'+k+'">'+v+'</a>'
				list.insert(i, str)
				i += 1
			# ensure_ascii 存放为中文
			json_str = json.dumps(list,ensure_ascii=False)
			fput.write(json_str)
			
			fput.close()
		# 提出队列
		q.task_done()