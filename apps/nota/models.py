from django.db import models
from apps.curso.models import Curso
from django.contrib.auth.models import User

# Create your models here.
class TipoEvaluacion(models.Model):
    nombre_tipo_evaluacion = models.CharField(max_length=30, blank=True, null=True)
    
class Evaluacion(models.Model):
    curso = models.ManyToManyField(Curso)
    tipo_evaluacion = models.ManyToManyField(TipoEvaluacion)
    peso = models.IntegerField(blank=True, null=True)

class NotaAlumno(models.Model):
    alumno = models.ManyToManyField(User)
    evaluacion = models.ManyToManyField(Evaluacion)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)