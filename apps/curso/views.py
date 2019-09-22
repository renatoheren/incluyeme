from django.shortcuts import render
from rest_framework import viewsets, generics
from . import models
from . import serializers

# Create your views here.
class MatriculaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.MatriculaSerializer

    def get_queryset(self):
        queryset = models.Matricula.objects.all()
        alumno = self.request.query_params.get('alumno', None)
        if alumno is not None:
            queryset = queryset.filter(alumno__username=alumno)
        return queryset