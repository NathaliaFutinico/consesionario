from rest_framework import serializers
from .models import Ventaxvehiculo


class VentaxvehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ventaxvehiculo
        fields = '__all__'
