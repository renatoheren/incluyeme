from rest_framework import serializers
from . import models

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evaluacion
        fields = '__all__'

class NotaAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotaAlumno
        fields = '__all__'