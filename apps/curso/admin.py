from django.contrib import admin
from apps.curso.models import Curso

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Curso, CursoAdmin)
