from rest_framework import serializers
from . import models

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clase
        fields = '__all__'