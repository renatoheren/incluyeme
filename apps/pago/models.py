from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pago(models.Model):
    concepto = models.CharField(max_length=30, blank=True, null=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)
    realizado = models.IntegerField(blank=True, null=True)

class PagoAlumno(models.Model):
    alumno = models.ManyToManyField(User)
    pago = models.ManyToManyField(Pago)