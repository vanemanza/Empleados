from django.urls import URLPattern, path

from .views import *

app_name = 'personas_app'

urlpatterns = [
     path('home/', HomeListView.as_view(), name='home'),
     path('lista_empleados/', EmpleadosListView.as_view(), name='lista_empleados' ),
     path('lista_por_area/<departamento>', EmpleadosPorAreaListView.as_view(), name='lista_por_area' ),
     path('lista_por_nombre', EmpleadosPorNombre.as_view(), name='lista_por_nombre' ),
     path('habilidades', HabilidadesList.as_view(), name='habilidades'),
     path('empleados_por_trabajos', EmpleadosPorTrabajoListView.as_view(), name='empleados_por_trabajos'),
     path('empleado_detalle/<pk>/', EmpleadoDetailView.as_view(), name='empleado_detalle'),
     path('registrar_empleado/', EmpleadoCreateView.as_view(), name='registrar_empleado'),
     path('registro_exitoso', RegistroExitoso.as_view(), name='registro_exitoso'),
     path('actualizar/<pk>', EmpleadoUpdateView.as_view(), name='actualizar'),
     path('eliminar/<pk>', EmpleadoDeleteView.as_view(), name='eliminar'),
]