# -*- coding: utf-8 -*-

import re

str='联系人：俞经理 手机：13911723056 固话：010-63872376 邮箱：bjzqxsj@163.com 网址： 公司网址：http://www.snewcen.com/home.html 公司地址：北京市丰台区五里店259号,外运陆运公司办公楼四层'
m = re.findall(u'([^\uff1a]+?)\uff1a([^\s]+)', str)

for k,v in m:
	s = '%s:%s' % (k,v)
	print(s)