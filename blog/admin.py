# -*- coding:utf-8 -*-
from django.contrib import admin

from models import *


# Register your models here.



# class ArticleAdmin(admin.ModelAdmin):
#    fields = ('title', 'desc', 'content',)


class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'content',)
    fieldsets = (
        (None, {'fields': ('title', 'desc', 'content',)}),
        ('高级设置', {'classes': ('collapse',), 'fields': (
            'click_count',
            'is_recommend',)}),
    )


class Media:
    js = (
        '',
        '',
        '/static/js/kindeditor-4.1.7/kind',
    )

admin.site.register(User)

admin.site.register(Tag)

admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)

admin.site.register(Comment)

admin.site.register(Links)

admin.site.register(Ad)
