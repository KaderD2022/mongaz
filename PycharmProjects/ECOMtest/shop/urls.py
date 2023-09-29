

from django.contrib import admin
from django.urls import path, include

from shop.views import index, detail

urlpatterns = [
    path('', index, name="home"),
    path('<int:myid>', detail, name="get"),
]
