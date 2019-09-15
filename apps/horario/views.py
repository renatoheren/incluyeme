from django.shortcuts import render
from rest_framework import viewsets, generics
from . import models
from . import serializers

# Create your views here.
class ClaseViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ClasesAlumnoSerializer

    def get_queryset(self):
        queryset = models.ClasesAlumno.objects.all()
        alumno = self.request.query_params.get('alumno', None)
        start  = self.request.query_params.get('start', None)
        end    = self.request.query_params.get('end', None)
        if alumno is not None:
            queryset = queryset.filter(alumno=alumno,clase__fecha__range=[start, end])
        return queryset