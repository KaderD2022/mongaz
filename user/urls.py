from django.urls import path
from user.views import index, my_view, logout_view, register_view, detail

urlpatterns = [
    path('', index, name="home"),
    path('login/', my_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('detail/<slug>/', detail, name="detail"),

  #  path('<int:myid>/', detail, name="detail"),
 
]
