from django.contrib import admin
from apps.curso.models import Curso, Matricula

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_curso']

class MatriculaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cursos']

admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
