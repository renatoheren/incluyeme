from django.db import models
from apps.curso.models import Curso

# Create your models here.
class TipoClase(models.Model):
    nombre_tipo_clase = models.CharField(max_length=30, blank=True, null=True)
    
class Clase(models.Model):
    curso = models.ManyToManyField(Curso)
    tipo_clase = models.ManyToManyField(TipoClase)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    presencial_online = models.SmallIntegerField(blank=True, null=True)
    aula = models.CharField(max_length=5, blank=True, null=True)