from django.db import models

# Create your models here.
# 创建一个 Preson 类 继承自 models.Model
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name
