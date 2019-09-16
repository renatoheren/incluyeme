from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class PagoViewset(viewsets.ModelViewSet):  
    serializer_class = serializers.PagoSerializer

    def get_queryset(self):
        queryset = models.Pago.objects.all()
        alumno = self.request.query_params.get('alumno', None)
        if alumno is not None:
            queryset = queryset.filter(alumno__username=alumno)
        return queryset