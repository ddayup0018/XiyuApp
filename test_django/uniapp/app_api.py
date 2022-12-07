from django.urls import path
from . import views

urlpatterns = [
    path("login/",views.login),
    path("register/",views.register),
    path("gettaocanlist/",views.gettaocanlist),
    path("getjishilist/",views.getjishilist),
    path("getdinglist/",views.getdinglist),
]