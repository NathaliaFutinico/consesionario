from rest_framework import serializers
from .models import Tipovehiculo


class TipovehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipovehiculo
        fields = '__all__'
