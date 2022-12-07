
from django.db import models

class Users(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = "用户表"
    
    username=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')

   
class Taocan(models.Model):
    class Meta:
        db_table = 'taocan'
        verbose_name = "套餐表"
    
    tc_pic=models.CharField(max_length=128,verbose_name="套餐图片",default="logo.png")
    tc_name=models.CharField(max_length=32,verbose_name="套餐名称")
    tc_sale=models.IntegerField(verbose_name="已售",default=0)
    tc_price=models.DecimalField(max_digits=6,decimal_places=2,verbose_name="套餐价格",null=False)
    tc_time=models.IntegerField(verbose_name="套餐时间")
    tc_intraduce=models.CharField(max_length=128,verbose_name="套餐介绍")

    
class Jishi(models.Model):
    class Meta:
        db_table = 'jishi'
        verbose_name = "技师表"
    
    js_pic=models.CharField(max_length=128,verbose_name="技师图片",default="logo.png")
    js_name=models.CharField(max_length=32,verbose_name="技师名称")
    js_from=models.CharField(max_length=32,verbose_name="技师来自")
    js_specialty=models.CharField(max_length=32,verbose_name="技师特长")
    js_status=models.CharField(max_length=4, verbose_name="技师状态",default="空闲")
    

    
class Dingdan(models.Model):
    class Meta:
        db_table = "dingdan"
        verbose_name = "用户订单表"
        
    user = models.ForeignKey(to=Users, related_name='dingdan_fortaocan',on_delete=models.CASCADE)
    taocan = models.ForeignKey(to=Taocan, related_name='dingdan_fortaocan',on_delete=models.PROTECT)
    jishi = models.ForeignKey(to=Jishi, related_name='dingdan_forjishi',on_delete=models.PROTECT)
    ding_status = models.CharField(max_length=6, verbose_name="订单状态")
    startServer = models.BooleanField(default=False,verbose_name="是否开始服务")
    
