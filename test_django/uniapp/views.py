from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.signing import TimestampSigner
from .models import Dingdan, Taocan, UserDetail,Jishi
import json
from django.core import serializers
from django.forms import model_to_dict
from django.core.cache import cache
from tools.mycache import cache_set

def login(request):
    data = json.loads(request.body)
    print(data)
    user = authenticate(**data)
    
    if user:
        
        ret_data = {"username":user.username}
        token = TimestampSigner(sep='.').sign_object(ret_data)
        ret_data['token'] = token
        ret_data['uid'] = user.id
        ret = {"code":1,"msg":ret_data}
        # cache.set('userinfo_cache',ret_data)
    else:
        ret = {"code":0,"msg":"用户名密码错误"}
    return JsonResponse(ret,safe=False)

def register(request):
    data = json.loads(request.body)
    user = User.objects.filter(username=data["username"]).first()
    
    if user:
        ret = {"code":0,"msg":"用户名已存在"}
        return JsonResponse(ret,safe=False)  
    else:
        new_user = User.objects.create_user(username=data["username"],password=data["password"])
        UserDetail.objects.create(user_id=new_user.id,telphone=data["telphone"])
        ret = {"code":0,"msg":"注册成功"}
        return JsonResponse(ret,safe=False)
 
@cache_set(60)   
def gettaocanlist(request):
    taocan = Taocan.objects.all().values()
    # print(taocan)
    ret_data = list(taocan)
    print(ret_data)
    ret = {"code":1,"msg":ret_data}
    return JsonResponse(ret,safe=False)

@cache_set(60)
def getjishilist(request):
    # myca = cache.get('userinfo_cache')
    # print(myca)
    jishi = Jishi.objects.all().values()
    # print(taocan)
    ret_data = list(jishi)
    print(ret_data)
    ret = {"code":1,"msg":ret_data}
    return JsonResponse(ret,safe=False)

@cache_set(60)
def getdinglist(request):
    # 拿到get请求的用户id
    uid = request.GET.get("uid")
    print(uid)
    # 通过用户id拿到用户订单(订单不止一个)
    dingdans = Dingdan.objects.filter(user_id = uid)
    
    ret_data_list = []
    for dingdanone in dingdans:
        # 利用queryset循环处理每一个订单
        # 将一个订单的订单信息、订单绑定的套餐信息、订单绑定的技师信息分别处理成字典
        dict3 = model_to_dict(dingdanone.jishi)
        dict2 = model_to_dict(dingdanone.taocan)
        dict1 = model_to_dict(dingdanone)
        
        # 合并三个字典
        dict_data = dict(dict3,**dict(dict2,**dict1))
        # print(dict_data)
        # 将字典加入到列表
        ret_data_list.append(dict_data)
        
        
    print(ret_data_list)
    ret = {"code":1,"msg":ret_data_list}
    return JsonResponse(ret,safe=False)