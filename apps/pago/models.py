from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boleta(models.Model):
    concepto = models.CharField(max_length=30, blank=True, null=True)
    fecha_vencimiento = models.DateTimeField(blank=True, null=True)

class Pago(models.Model):
    REALIZADO = (
        ('Si', 'Si'),
        ('No', 'No')
    )
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    realizado = models.CharField(max_length=2, choices=REALIZADO)