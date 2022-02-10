from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import DaySerializer, TrainingSerializer, MeasurementSerializer, UserSerializer
from .models import Day, Training, Measurement


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class DayListView(generics.ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = (AllowAny,)


class DayRetrieveView(generics.RetrieveAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = (AllowAny,)


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'id']


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


class MeasurementListView(generics.ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = (AllowAny,)


class MeasurementRetrieveView(generics.RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = (AllowAny,)


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['chest', 'left_arm', 'right_arm', 'weight']

