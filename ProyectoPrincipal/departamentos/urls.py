from django.urls import path
#from .views import departamento
from .views import NuevoDepartamentoView, DepartamentosView
#from django.views.generic import TemplateView

# urlpatterns = [   
#     path('', departamento, name='departamentos'),
# ]

urlpatterns = [   
    path('', DepartamentosView.as_view(), name='inicio'),
    path('nuevo/', NuevoDepartamentoView.as_view(), name='crear_departamento'),
]

