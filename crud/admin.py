from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author','email','date')
admin.site.register(Article, ArticleAdmin)