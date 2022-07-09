from django.urls import path
from .views import *

urlpatterns = [ 
    #path('', Prueba.as_view(), name='prueba'),
    path('lista/', PruebaListView.as_view(), name='prueba_lista'),
    path('lista-prueba/', ListarPruebaListView.as_view(), name='lista'),
    path('agregar/', PruebaCreateView.as_view(), name='agregar'),
    path('productos', ProductList.as_view(), name='listado_productos')
]