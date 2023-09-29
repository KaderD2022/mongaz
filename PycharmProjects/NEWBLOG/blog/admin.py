from django.contrib import admin

from blog.models import Category, Post, Comment, Reponse


# Register your models here.


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'slug')
    filter = ('name', 'slug')
    list_filter = ('name', 'slug')


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created', 'updated', 'status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('author', 'status', 'created')
    filter = ('author', 'status', 'created', 'publish')
    list_filter = ('author', 'status', 'created', 'publish')



class AdminComment(admin.ModelAdmin):
    list_display = ('username', 'email', 'created', 'updated')


class AdminReponse(admin.ModelAdmin):
    list_display = ('username', 'email', 'created', 'updated')



admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)
admin.site.register(Reponse, AdminReponse)