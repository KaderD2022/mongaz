from django.contrib import admin

# Register your models here.
from myblog.models import Post, Comment, Category


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated', 'status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('author', 'status', 'created')
    filter = ('author', 'status', 'created', 'publish')
    list_filter = ('author', 'status', 'created', 'publish')


class AdminComment(admin.ModelAdmin):
    list_display = ('username', 'email', 'created', 'updated')


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
admin.site.register(Category, AdminCategory)
