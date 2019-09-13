from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class ClaseViewset(viewsets.ModelViewSet):
    queryset = models.Clase.objects.all()
    serializer_class = serializers.ClaseSerializer