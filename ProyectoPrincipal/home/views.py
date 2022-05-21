from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.
# class Prueba(TemplateView):
#     template_name = 'prueba.html'


class PruebaListView(ListView):
    template_name = "lista.html"
    context_object_name = 'listaNumeros'
    queryset = [1, 2, 3, 4, 5]


class ListarPruebaListView(ListView):
    template_name = "lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "add.html"
    fields = '__all__'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "agregar.html"
    form_class = PruebaForm
    success_url = '/'
    