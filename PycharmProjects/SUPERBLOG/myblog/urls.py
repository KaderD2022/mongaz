from django.contrib import admin
from django.urls import path

from .views import index, detail
urlpatterns = [
    path('', index, name='home'),
    path('<slug>/', detail, name='detail'),
]
