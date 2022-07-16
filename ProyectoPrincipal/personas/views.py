from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  TemplateView, 
                                  UpdateView, 
                                  DeleteView)

from . models import Persona

# 0) Template Base - Home
class HomeListView(TemplateView):
    template_name = 'personas/home.html'
    #queryset = Persona.objects.all().order_by('apellido')
    #paginate_by = 7
    #context_object_name = 'lista'

    # def get_context_data(self, **kwargs):         
    #     context =  super().get_context_data(**kwargs)  
    #     return context

class EmpleadosListView(ListView):
    template_name = "personas/lista_empleados.html" #es la ruta donde está el archivo html con el q vamos a trabajar
    #queryset = Persona.objects.all().order_by('apellido')
    paginate_by = 7 # para optimizar la consulta y q no sea tan pesada, internamente tiene el parametro page=
    ordering = 'apellido'
    model = Persona #listView requiere un modelo
    context_object_name = 'lista' #nombre del objeto a traves del cual accedo en html -> {{lista}}
    #listView : la vista se retorna x defecto en un object list, x eso no hace falta pasarle el context_object_name
    
    # def get_context_data(self, **kwargs): 
    #     context =  super().get_context_data(**kwargs)# este es el contexto q enviamos al template
    #     print(context)
    #     # el contexto posee los siguientes objetos:
    #         # paginator
    #         # page_obj
    #         # is_paginated
    #         # object_list
    #     return context

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        lista = Persona.objects.filter(
            nombre__icontains=palabra_clave
        )
        return lista 
   

# 2) listar todos los empleados q pertenecen a un area de la empresa
# class EmpleadosPorAreaListView(ListView):
#     """ lista empleados de una empresa por areas"""
#     queryset = Persona.objects.filter(departamento__nombre='area contable') # no es muy eficiente xq le tengo q indicar en el filtro el area cada vez
#     template_name = "lista_por_area.html"

class EmpleadosPorAreaListView(ListView):
    """ lista empleados de una empresa por areas"""
    #model = Persona
    # en vez de model puedo usar atributo queryset para filtrar segun lo q necesite y no toda la lista
    #queryset = Persona.objects.filter(departamento__nombre='area contable') # no es muy eficiente xq le tengo q indicar en el filtro el area cada vez
    #en vez de usar atributo queryset, uso metodo get_queryset q retorna una lista
    template_name = "personas/lista_por_area.html"
    context_object_name = 'lista'

    def get_queryset(self):
        # puedo sobreescribir el metodo q trae x defaul el ListView
        # retorna una lista de elementos
        # el valor devuelto debe ser un iterable o una instancia del queryset
        area = self.kwargs['departamento'] # recupero el parametro q me envian por url!
        lista = Persona.objects.filter(departamento__nombre=area) # departamento es otra tabla y nombre es el atr q necesito de la rel
        return lista


# 3) listar empleados por trabajo
    # para hacer de tarea, como práctica

class EmpleadosPorTrabajoListView(ListView):
    #model = Persona
    template_name = "personas/empleados_por_trabajo.html"
    #context_object_name = 'lista_puesto'

    def get_queryset(self):
        puesto = self.request.GET.get("trabajo", "")        
        lista = Persona.objects.filter(puesto=puesto)
        return lista          


# 4) listar los empleados por palabra clave

class EmpleadosPorNombre(ListView):
    """
    Lista empleados por palabra clave
    """
    template_name = "personas/empleado_por_nombre.html"
    context_object_name = 'empleados'

    def get_queryset(self) : # función donde haré el filtro!
        print('***************************************')
        palabra_clave = self.request.GET.get("kword", "") # del objeto request recupero lo q tenga metodo GET con get
        lista = Persona.objects.filter(nombre=palabra_clave)
        print(f'---- lista resultado: {lista}-------------')
        return lista



# 5) listar habilidades de un empleado

class HabilidadesList(ListView):
    template_name = 'personas/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # el atributo habilidades es un ManyToMany con la tabla Habilidades
        # primero debo obtener un REGISTRO de un empleado y no un queryset
        # para cada empleado recuperar su lista de habilidades
        id_empleado = self.request.GET.get("id_empleado", "")
        empleado = Persona.objects.get(id=id_empleado)      
        return empleado.habilidad.all()


class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "personas/detalles_empleado.html"

    # def get_object(self, queryset: Optional[models.query.QuerySet[_M]] = ...) -> _M: #redefine la forma de recuperar un objeto
    #     return super().get_object(queryset)


    def get_context_data(self, **kwargs): # envia alguna variable extra hacia el template,alguna q no esté dentro de los atrs del modelo
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del Mes'
        #debo crear un proceso para determinar si el context es un empleado del mes o no
        return context

class RegistroExitoso(TemplateView):
    template_name = "personas/registro_exitoso.html"


class EmpleadoCreateView(CreateView):
    template_name = "personas/registrar_empleado.html"
    model = Persona       
    fields = [
        'nombre', 
        'apellido',
        'puesto',
        'departamento',
        'habilidad'
    ]
    success_url = reverse_lazy('personas_app:registro_exitoso')    

    def form_valid(self, form): # esto no es lo ideal!
        empleado = form.save() #creo una instancia de empleado con los datos validos del formulario y ya está en la bd
        empleado.fullname = f'{empleado.nombre} {empleado.apellido}'
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Persona
    template_name = "personas/actualizar.html"
    fields = [
        'nombre', 
        'apellido',
        'puesto',
        'departamento',
        'habilidad'
    ]
    success_url= reverse_lazy('personas_app:registro_exitoso')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        # el código q coloco acá solo se ejecuta una vez q se validó q el form es válido
        # cuando lo interceptamos, ya sabemos q el formulario es válido
        # puede ocurrir q necesite interceptar el post antes de q se haya validado el formulario
        self.object = form.save()
        print(f'--------------form valid--------------')        
        return super(EmpleadoUpdateView, self).form_valid(form)    

    def post(self, request, *args, **kwargs):
        # en el post aun no hemos validado los datos
        self.object = self.get_object()
        print(f'--------------post--------------')
        datos = request.POST
        nombre = request.POST['nombre']
        print(f'============={nombre}===============')
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = "personas/eliminar.html"
    success_url= reverse_lazy('personas_app:registro_exitoso')    

           