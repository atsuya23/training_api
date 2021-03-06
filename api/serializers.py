from rest_framework import serializers
from .models import Training
from django.contrib.auth.models import User
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Training
        fields = '__all__'



