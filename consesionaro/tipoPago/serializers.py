from rest_framework import serializers
from .models import Tipodepago


class TipodepagoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipodepago
        fields = '__all__'
