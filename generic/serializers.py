from rest_framework import serializers
from .models import Car


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', )


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'description')


class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'description')