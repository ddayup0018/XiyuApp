from rest_framework.routers import DefaultRouter  
from . import views
from django.urls import path,re_path

router = DefaultRouter()
router.register("users", views.UsersView, basename="users")  
router.register("taocan", views.TaocanView, basename="taocan")  
router.register("jishi", views.JishiView, basename="jishi")  
router.register("dingdan", views.DingdanView, basename="dingdan") 
urlpatterns = [
    re_path(r'^ufd/(?P<pk>[0-9]+)/$', views.UserForDingdanView.as_view()),
] + router.urls  