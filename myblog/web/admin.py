from django.contrib import admin
# 引入自己的class
from .models import Article, Person

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	# 配置要显示的字段的，当然也可以显示非字段内容，或者字段相关的内容
    list_display = ('title','pub_date','update_time',)
admin.site.register(Article,ArticleAdmin)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_data',)
	# 搜索功能
	search_fields = ('name',)
	# 筛选
	list_filter = ('age',)
	# 定制加载的列表(特定的用户加载特定的列表) 重写get_queryset方法
	def get_queryset(self, request):
		# super 解决多重继承的问题
		qs = super(PersonAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(author=request.user)
	# 定制搜索  queryset 是默认的结果，search_term 是在后台搜索的关键词
	def get_search_results(self, request, queryset, search_term):
		queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
		try:
			search_term_as_int = int(search_term)
			queryset |= self.model.objects.filter(age=search_term_as_int)
		except:
			pass
		return queryset, use_distinct
admin.site.register(Person, PersonAdmin)

