from rest_framework.views import APIView,Response
from rest_framework.viewsets import ModelViewSet  # 导入framework提供的视图类
from uniapp.models import Taocan,Jishi,Dingdan
from .serializers import TaocanSerializer,JishiSerializer,DingdanSerializer


# Create your views here.
class TaocanView(ModelViewSet):
    
    # 此处只需提供2个属性(ModelViewSet里为我们提供了增删改查等功能)
    queryset = Taocan.objects.all()  # 转换所有数据(筛选数据有兴趣的自己可以写)
    serializer_class = TaocanSerializer  # （序列化器指定）转换指定的字段，在序列化器里定义的

class JishiView(ModelViewSet):
    # 此处只需提供2个属性(ModelViewSet里为我们提供了增删改查等功能)
    queryset = Jishi.objects.all()  # 转换所有数据(筛选数据有兴趣的自己可以写)
    serializer_class = JishiSerializer  # （序列化器指定）转换指定的字段，在序列化器里定义的

class DingdanView(ModelViewSet):
    # 此处只需提供2个属性(ModelViewSet里为我们提供了增删改查等功能)
    queryset = Dingdan.objects.all()  # 转换所有数据(筛选数据有兴趣的自己可以写)
    serializer_class = DingdanSerializer  # （序列化器指定）转换指定的字段，在序列化器里定义的

class UserForDingdanView(APIView):

    def get_object(self,pk):
        return Dingdan.objects.filter(user_id = pk)

    def get(self, request, format=None,pk=None):
        dingdans = self.get_object(pk)
        serializer = DingdanSerializer(dingdans, many=True)
        return Response(serializer.data)