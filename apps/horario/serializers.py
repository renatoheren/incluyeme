from rest_framework import serializers
from . import models
from apps.curso.serializers import CursoSerializer

class ClaseSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(many=False, read_only=True)
    class Meta:
        model = models.Clase
        fields = '__all__'


class ClasesAlumnoSerializer(serializers.ModelSerializer):
    clase = ClaseSerializer(many=False, read_only=True)

    class Meta:
        model = models.ClasesAlumno
        fields = '__all__'