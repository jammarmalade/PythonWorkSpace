#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
	return HttpResponse(u'<h1>Hello World!</h1>我的第一个python网页')
# 加法
def add(request):
	# 获取 get 参数 a ,没有就默认为 0
	a = request.GET.get('a',0)
	# 另一种获取方式，最好是
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))
# 优化的 url
def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

# 获取对应的网址
from django.core.urlresolvers import reverse
def getAddress(request):
	# add2 就是在 urls.py 中定义的 name
	str = reverse('add2', args=(4,5))
	'''
	在模板中这样调用
	<a href="{% url 'add2' 4 5 %}">link</a>
	生成这样的 链接
	<a href="/add/4/5/">link</a>
	'''
	return HttpResponse(str)

'''
跳转函数
访问
http://127.0.0.1:8000/add2/5/6/
会调转到
http://127.0.0.1:8000/new_add/5/6/
'''
from django.http import HttpResponseRedirect
def redirect_add2(request, a, b):
	return HttpResponseRedirect(
		reverse('add2', args=(a, b))
	)

# 使用模板
# render 分配变量给模板
from django.shortcuts import render
from web.models import Person
def home(request):
	str = u'This is my site home page'
	# for 循环和 list 列表的使用
	testList = ['php','python','javascript','jquery','html']
	# dict
	testDict = {'php':'学过了','python':'正在学'}
	# 条件判断 一个长度为100 的list ; map 函数 ，类似 php 的 array_map
	tList = range(100)
	# 变量，逻辑操作
	tVar = 24
	# -----------------操作数据库---------------
	# ------------------插入-------------------
	'''
	# 插入 ，返回一个 dict , PS1.id, PS1.name, PS1.age
	PS1 = Person.objects.create(name='jam',age=20)
	# 打印 对象的所有属性
	#print(PS1.__dict__)
	# 第二种插入，返回一个 dict , PS2.id, PS2.name, PS2.age
	PS2 = Person(name="jam00", age=21)
	PS2.save()
	# 第三种插入，返回一个 dict , PS3.id, PS3.name, PS3.age
	PS3 = Person()
	PS3.name = 'jam11'
	PS3.age = 22
	PS3.save()
	# 第四种插入，会判断 name 是否存在，不存在才插入，速度要相对慢些，返回一个元组，第一个为Person对象，第二个为True或False, 新建时返回的是True, 已经存在时返回False
	PS4 = Person.objects.get_or_create(name="jam22", age=24)
	# (<Person: jam22>, False)
	'''
	# ------------------获取-------------------
	# 第一种获取，获取所有，返回 类似 php 的二维数组 字段=>值
	get1 = Person.objects.all()
	# 第二种获取，只是在第一种上面做了切片 [ 从那里开始 : 到哪里结束 : 步长]
	get2 = Person.objects.all()[:2]
	# 第三种获取，get 用于获取单条数据，精确查找
	get3 = Person.objects.get(name='jam00')
	# 第四种获取，获取满足条件的数据，filter
	get4 = Person.objects.filter(name__contains="jam")      # 名称中包含 "jam"的人 , __icontains 为不区分大小写
	get4_1 = Person.objects.filter(name__regex="0$")        # 名称中包含 "0"的人 , __iregex 为不区分大小写
	# 第五种获取，排除符合某些条件的数据
	get5 = Person.objects.exclude(name__contains="11")      # 排除名称中包含 11 的用户
	get5_1 = Person.objects.filter(name__contains="jam").exclude(age=20) # 找出名称含有 jam , 但是排除年龄是20的
	

	return render(request, 'home.html',{
		'title':str,
		'testList':testList,
		'testDict':testDict,
		'tList':tList,
		'tVar':tVar,
		# 'PS1':PS1,
		# 'PS2':PS2,
		# 'PS3':PS3,
		# 'PS4':PS4,
		'get1':get1,
		'get2':get2,
		'get3':get3,
		'get4':get4,
		'get4_1':get4_1,
		'get5':get5,
		'get5_1':get5_1,
	})











