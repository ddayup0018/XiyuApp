from rest_framework.routers import DefaultRouter  # 使用rest_framework生成路由
from backadmin import views
from django.urls import re_path

router = DefaultRouter()
router.register("taocan", views.TaocanView, basename="taocan")  # 为我们生成5个接口地址
router.register("jishi", views.JishiView, basename="jishi")  # 为我们生成5个接口地址
router.register("dingdan", views.DingdanView, basename="dingdan")  # 为我们生成5个接口地址
urlpatterns = [
    re_path(r'^ufd/(?P<pk>\d+)/$',views.UserForDingdanView.as_view())
] + router.urls  # 拼接路由
