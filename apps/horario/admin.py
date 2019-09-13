from django.contrib import admin
from apps.horario.models import Clase, TipoClase

# Register your models here.
class ClaseAdmin(admin.ModelAdmin):
    pass

class TipoClaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Clase, ClaseAdmin)
admin.site.register(TipoClase, TipoClaseAdmin)
