from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class PagoAlumnoViewset(viewsets.ModelViewSet):
    queryset = models.PagoAlumno.objects.all()
    serializer_class = serializers.PagoAlumnoSerializer