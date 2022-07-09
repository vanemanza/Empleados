from django.urls import path
#from .views import departamento
from .views import NuevoDepartamentoView, DepartamentosView
#from django.views.generic import TemplateView

# urlpatterns = [   
#     path('', departamento, name='departamentos'),
# ]
app_name = 'departamentos_app'

urlpatterns = [   
    path('', DepartamentosView.as_view(), name='departamentos'),
    path('nuevo/', NuevoDepartamentoView.as_view(), name='crear_departamento'),
]

