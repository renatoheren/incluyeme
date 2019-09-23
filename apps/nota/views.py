from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class EvaluacionViewset(viewsets.ModelViewSet):
    queryset = models.Evaluacion.objects.all()
    serializer_class = serializers.EvaluacionSerializer

class NotaAlumnoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.NotaAlumnoSerializer

    def get_queryset(self):
        queryset = models.NotaAlumno.objects.all()
        alumno = self.request.query_params.get('alumno', None)
        if alumno is not None:
            queryset = queryset.filter(alumno__username=alumno)
        return queryset