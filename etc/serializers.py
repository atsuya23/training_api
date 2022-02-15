from rest_framework import serializers
from .models import Memo, Goal, Measurement


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = '__all__'