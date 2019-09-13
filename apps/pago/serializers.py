from rest_framework import serializers
from . import models

class PagoAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PagoAlumno
        fields = '__all__'