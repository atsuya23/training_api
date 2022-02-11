from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .models import DayEtc, Memo, Goal
from .serializers import MemoSerializer, DayEtcSerializer, GoalSerializer


class DayEtcViewSet(viewsets.ModelViewSet):
    queryset = DayEtc.objects.all()
    serializer_class = DayEtcSerializer
    permission_classes = (AllowAny,)


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['day_etc', 'length', 'deadline']


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    permission_classes = (AllowAny,)


