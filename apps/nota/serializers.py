from rest_framework import serializers
from . import models
from apps.curso.serializers import CursoSerializer

class TipoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoEvaluacion
        fields = '__all__'

class EvaluacionSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(many=False, read_only=True)
    tipo_evaluacion = TipoEvaluacionSerializer(many=False, read_only=True)
    class Meta:
        model = models.Evaluacion
        fields = '__all__'

class NotaAlumnoSerializer(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer(many=False, read_only=True)
    class Meta:
        model = models.NotaAlumno
        fields = '__all__'