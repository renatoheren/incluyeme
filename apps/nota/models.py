from django.db import models
from apps.curso.models import Curso
from django.contrib.auth.models import User

# Create your models here.
class TipoEvaluacion(models.Model):
    nombre_tipo_evaluacion = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre_tipo_evaluacion
    
class Evaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo_evaluacion = models.ForeignKey(TipoEvaluacion, on_delete=models.CASCADE)
    peso = models.IntegerField(blank=True, null=True)

class NotaAlumno(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)