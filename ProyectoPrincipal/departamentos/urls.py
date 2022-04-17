from django.urls import path
from .views import departamento

urlpatterns = [   
    path('', departamento, name='departamentos'),
]
