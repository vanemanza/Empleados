from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.
# class Prueba(TemplateView):
#     template_name = 'prueba.html'


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = [1, 2, 3, 4, 5]


class ListarPruebaListView(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/agregar.html"
    fields = '__all__'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/agregar.html"
    form_class = PruebaForm
    success_url = reverse_lazy('prueba_lista')
    