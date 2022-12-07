from django.contrib import admin
from .models import UserDetail
from .models import Taocan,Jishi,Dingdan

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Taocan)
admin.site.register(Jishi)
admin.site.register(Dingdan)
