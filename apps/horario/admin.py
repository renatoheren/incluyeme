from django.contrib import admin
from apps.horario.models import Clase, TipoClase, ClasesAlumno

# Register your models here.
class ClaseAdmin(admin.ModelAdmin):
    pass

class TipoClaseAdmin(admin.ModelAdmin):
    pass

class ClasesAlumnoAdmin(admin.ModelAdmin):
    search_fields = ['alumno']
    autocomplete_fields = ['alumno']

admin.site.register(Clase, ClaseAdmin)
admin.site.register(TipoClase, TipoClaseAdmin)
admin.site.register(ClasesAlumno, ClasesAlumnoAdmin)
