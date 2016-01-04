from django.db import models

# Create your models here.
# 创建一个 Preson 类 继承自 models.Model
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name
	# 自定义要显示的数据
	def my_property(self):
		return self.name + ' - ' + str(self.age)
	# 标题
	my_property.short_description = u"一条数据"
	full_data = property(my_property)

class Article(models.Model):
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')

	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
	update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
	# 定义 Model 的时候 写一个 __str__ 函数，若直接显示这个对象， 那么显示的就是这个值
	def  __str__(self):
		return self.title
