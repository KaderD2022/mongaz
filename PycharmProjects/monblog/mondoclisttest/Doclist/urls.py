from django.contrib import admin
from django.urls import path
from list import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add-collection/', views.add_collection, name="add-collection"),
    path('add-task/', views.add_task, name="add-task"),
    path('admin/', admin.site.urls),
]



