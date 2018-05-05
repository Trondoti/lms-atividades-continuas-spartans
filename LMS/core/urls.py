from django.urls import path, include
from django.conf.urls import url, include
from .views import login
urlpatterns = [
     path('login/', login, name="login"),
]
