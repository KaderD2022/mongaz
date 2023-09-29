from django.contrib import admin
from django.urls import path

from myblog.views import post_detail, list_post

urlpatterns = [
    path('', list_post, name="home"),
    path('category/<slug:category>/', list_post, name="category_home"),
    path('<slug>/', post_detail, name="post-detail"),
    # path('', PostListView.as_view(), name="home"),
]
