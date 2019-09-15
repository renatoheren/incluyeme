from django.contrib import admin
from apps.pago.models import Pago, Boleta

# Register your models here.
class PagoAdmin(admin.ModelAdmin):
    pass

class BoletaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pago, PagoAdmin)
admin.site.register(Boleta, BoletaAdmin)
