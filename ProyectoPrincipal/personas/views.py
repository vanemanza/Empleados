from django.shortcuts import render

from django.views.generic import ListView

from . models import Persona

# 1) listar todos los empleados de la empresa
class EmpleadosListView(ListView):
    model = Persona
    template_name = "lista_empleados.html"
    #context_object_name = 'lista'


# 2) listar todos los empleados q pertenecen a un area de la empresa
# class EmpleadosPorAreaListView(ListView):
#     """ lista empleados de una empresa por areas"""
#     queryset = Persona.objects.filter(departamento__nombre='area contable') # no es muy eficiente xq le tengo q indicar en el filtro el area cada vez
#     template_name = "lista_por_area.html"

class EmpleadosPorAreaListView(ListView):
    """ lista empleados de una empresa por areas"""
    #queryset = Persona.objects.filter(departamento__nombre='area contable') # no es muy eficiente xq le tengo q indicar en el filtro el area cada vez
    #en vez de usar atributo queryset, uso metodo get_queryset q retorna una lista
    template_name = "lista_por_area.html"

    def get_queryset(self):
        # puedo sobreescribir el metodo q trae x defaul el ListView
        area = self.kwargs['departamento'] # recupero el parametro q me envian por url!
        lista = Persona.objects.filter(departamento__nombre=area)
        return lista


# 3) listar empleados por trabajo



# 4) listar los empleados por palabra clave



# 5) listar habilidades de un empleado