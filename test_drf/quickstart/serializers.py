from rest_framework import serializers
from .models import Taocan,Jishi,Dingdan,Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields = '__all__'

class TaocanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taocan
        fields = '__all__'

class JishiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jishi
        fields = '__all__'

class DingdanSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    taocan = TaocanSerializer()
    jishi = JishiSerializer()
    class Meta:
        model=Dingdan
        fields = '__all__'


