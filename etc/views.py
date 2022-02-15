from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .models import Memo, Goal, Measurement
from .serializers import MemoSerializer, GoalSerializer, MeasurementSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day', 'length', 'deadline']


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    permission_classes = (AllowAny,)


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


