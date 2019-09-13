from django.contrib import admin
from apps.pago.models import Pago, PagoAlumno

# Register your models here.
class PagoAdmin(admin.ModelAdmin):
    pass

class PagoAlumnoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pago, PagoAdmin)
admin.site.register(PagoAlumno, PagoAlumnoAdmin)
