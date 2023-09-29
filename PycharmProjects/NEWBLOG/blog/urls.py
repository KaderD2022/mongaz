from django.contrib import admin
from django.urls import path
from .views import index, detail, post_search

urlpatterns = [
    path('', index, name='home'),
    path('search/', post_search, name="post_search"),
    path('category/<slug:category>/', index, name="category_home"),
    path('<slug>/', detail, name="detail"),



]




