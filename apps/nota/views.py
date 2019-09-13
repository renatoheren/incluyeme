from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class EvaluacionViewset(viewsets.ModelViewSet):
    queryset = models.Evaluacion.objects.all()
    serializer_class = serializers.EvaluacionSerializer

class NotaAlumnoViewset(viewsets.ModelViewSet):
    queryset = models.NotaAlumno.objects.all()
    serializer_class = serializers.NotaAlumnoSerializer