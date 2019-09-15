from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.nombre_curso