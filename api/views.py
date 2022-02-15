from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TrainingSerializer, UserSerializer
from .models import Training


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class TrainingListView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)


class TrainingRetrieveView(generics.RetrieveAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'type', 'phase', 'weight']


# ベンチのみ
class BenchAllViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.filter(type='benchPress')
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'phase', 'weight']


# ベンチ、高重量
class BenchHighWeightViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.filter(type='benchPress', phase="highWeight")
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'weight']


# ベンチ、低重量
class BenchLowWeightViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.filter(type='benchPress', phase="lowWeight")
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'weight']


# ベンチ、基本
class BenchNormalViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.filter(type='benchPress', phase="normal")
    serializer_class = TrainingSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'weight']



