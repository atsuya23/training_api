from rest_framework import serializers
from .models import DayEtc, Memo, Goal


class DayEtcSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayEtc
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'
