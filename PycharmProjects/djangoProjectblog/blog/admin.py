from django.contrib import admin

from blog.models import Post, Comment


# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'created', 'updated', 'status', 'author')
    search_fields = ('title', 'slug', 'body', 'created')
    prepopulated_fields = {'slug': ('title',)}
    filter = ('title', 'slug', 'body', 'created')
    filter_fields = ('title', 'slug', 'body', 'created', 'updated')


class AdminComment(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'body', 'created')
    search_fields = ('name', 'username', 'created')
    filter = ('name', 'username')
    filter_fields = ('name', 'username', 'body', 'created')


admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
