from rest_framework import routers
from apps.horario import views as horario_views
from apps.nota import views as nota_views
from apps.pago import views as pago_views
from apps.curso import views as curso_views

router = routers.DefaultRouter()
router.register(r'clases', horario_views.ClaseViewset, basename="clases")
router.register(r'cursos', curso_views.MatriculaViewset, basename="cursos")
router.register(r'notas', nota_views.NotaAlumnoViewset, basename="notas")
router.register(r'pagos', pago_views.PagoViewset, basename="pagos")