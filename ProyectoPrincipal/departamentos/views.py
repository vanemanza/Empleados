import imp
from django.shortcuts import render
#from django.views.generic import ListView

from .models import Departamento

# Create your views here.
# class Departamentos(ListView):
#     model = Departamento

def departamento(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos':departamentos,
    }
    return render(request, 'departamento.html', context,)
