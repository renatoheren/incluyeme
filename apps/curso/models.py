from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.nombre_curso

class Matricula(models.Model):
    cursos = models.ManyToManyField(Curso)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)