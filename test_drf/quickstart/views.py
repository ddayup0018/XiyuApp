from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView,Response
from .models import Taocan,Jishi,Dingdan,Users
from .serializers import TaocanSerializer,JishiSerializer,DingdanSerializer,UsersSerializer
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.mixins import ListModelMixin


class UsersView(ModelViewSet):
    queryset = Users.objects.all()  
    serializer_class = UsersSerializer  

class TaocanView(ModelViewSet):
    
    queryset = Taocan.objects.all()  
    serializer_class = TaocanSerializer  

class JishiView(ModelViewSet):
    
    queryset = Jishi.objects.all()  
    serializer_class = JishiSerializer

class DingdanView(ModelViewSet):
    
    queryset = Dingdan.objects.all()  
    serializer_class = DingdanSerializer

class UserForDingdanView(APIView):

    def get(self, request, format=None,pk=None):
        dingdans = Dingdan.objects.filter(user_id = pk)
        serializer = DingdanSerializer(dingdans, many=True)
        return Response(serializer.data)

# class EveryForDingdanView(ListAPIView):
#     queryset = Dingdan.objects.all()  
#     serializer_class = DingdanSerializer
    