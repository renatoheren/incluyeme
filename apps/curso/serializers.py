from rest_framework import serializers
from . import models

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True, read_only=True)
    class Meta:
        model = models.Matricula
        fields = '__all__'