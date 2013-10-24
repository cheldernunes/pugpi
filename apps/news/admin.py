# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Post, Category
from .forms import PostForm


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'updated_at', 'published_at', 'get_action']
    prepopulated_fields = {'slug': ('title',)}
    form = PostForm
    exclude = ('updated_at',)

    def get_action(self, action):
        return u'<a href="/%s" target="blank">Visualizar Post</a>' % action.get_absolute_url()
    get_action.allow_tags = True
    get_action.short_description = 'Ações'


admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
