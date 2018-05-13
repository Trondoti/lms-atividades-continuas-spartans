from django.urls import path, include
from django.conf.urls import url, include
from .views import login, logout
urlpatterns = [
     path('login/', login, name="login"),
     path('logout/', logout, name="logout"),
]
