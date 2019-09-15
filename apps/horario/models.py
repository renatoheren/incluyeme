from django.db import models
from apps.curso.models import Curso
from django.contrib.auth.models import User

# Create your models here.
class TipoClase(models.Model):
    nombre_tipo_clase = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nombre_tipo_clase
    
class Clase(models.Model):
    PRESENCIAL = (
        ('Presencial', 'Presencial'),
        ('Online', 'Online')
    )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    tipo_clase = models.ForeignKey(TipoClase, on_delete=models.CASCADE)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    presencial_u_online = models.CharField(max_length=10, choices=PRESENCIAL)
    aula = models.CharField(max_length=5, blank=True, null=True)

class ClasesAlumno(models.Model):
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)