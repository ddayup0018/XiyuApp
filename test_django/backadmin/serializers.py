from uniapp.models import Taocan,Jishi,Dingdan
from rest_framework import serializers


class TaocanSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Taocan
        fields = '__all__'


class JishiSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Jishi
        fields = '__all__'

class DingdanSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Dingdan
        fields = '__all__'