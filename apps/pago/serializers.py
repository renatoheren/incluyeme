from rest_framework import serializers
from . import models

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Boleta
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    boleta = BoletaSerializer(many=False, read_only=True)

    class Meta:
        model = models.Pago
        fields = '__all__'