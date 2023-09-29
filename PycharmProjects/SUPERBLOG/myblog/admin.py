from django.contrib import admin

from myblog.models import Post, Comment

# Register your models here.


""" 
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated', 'status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('author', 'status', 'created')
    filter = ('author', 'status', 'created', 'publish')
    list_filter = ('author', 'status', 'created', 'publish')
 """


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'created', 'updated', 'status', 'author')
    search_fields = ('title', 'slug', 'body', 'created')
    prepopulated_fields = {'slug': ('title',)}
    filter = ('title', 'slug', 'body', 'created')
    filter_fields = ('title', 'slug', 'body', 'created', 'updated')


class AdminComment(admin.ModelAdmin):
    list_display = ('username', 'email', 'created', 'updated')

admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)

