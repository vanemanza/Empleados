from django.urls import URLPattern, path

from .views import *

urlpatterns = [
     path('lista_empleados/', EmpleadosListView.as_view(), name='lista_empleados' ),
     path('lista_por_area/<departamento>', EmpleadosPorAreaListView.as_view(), name='lista_por_area' ),
     path('lista_por_palabra', EmpleadosPorKword.as_view(), name='lista_por_kword' ),
     path('habilidades', HabilidadesList.as_view(), name='habilidades'),
]