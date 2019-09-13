from django.contrib import admin
from apps.nota.models import Evaluacion, NotaAlumno, TipoEvaluacion

# Register your models here.
class EvaluacionAdmin(admin.ModelAdmin):
    pass

class NotaAlumnoClaseAdmin(admin.ModelAdmin):
    pass

class TipoEvaluacionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Evaluacion, EvaluacionAdmin)
admin.site.register(NotaAlumno, NotaAlumnoClaseAdmin)
admin.site.register(TipoEvaluacion, TipoEvaluacionAdmin)
