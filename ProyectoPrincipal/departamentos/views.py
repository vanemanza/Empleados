import imp
from django.shortcuts import render
#from django.views.generic import ListView
# uso el formView en vez de createView xq no voy a trabajar con modelos
from django.views.generic.edit import FormView
from .forms import NuevoDepartamentoForm
#from .models import Departamento
from personas.models import Persona
from departamentos.models import Departamento
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy



# Create your views here.
# class Departamentos(ListView):
#     model = Departamento

# def departamento(request):
#     departamentos = Departamento.objects.all()
#     context = {
#         'departamentos':departamentos,
#     }
#     return render(request, 'departamento.html', context,)

class DepartamentosView(ListView):
    template_name = "departamentos/home.html"
    model = Departamento
    context_object_name = 'departamentos'
    paginate_by = 5

class NuevoDepartamentoView(FormView):
    template_name = 'departamentos/departamento.html'
    form_class = NuevoDepartamentoForm
    success_url = reverse_lazy('departamentos')    

    def form_valid(self, form):
        print(f'----- estamos en el form valid----------------------')
        # con form valid recupero los datos validados en el formulario
        departamento = Departamento(
            nombre = form.cleaned_data['departamento']
        )
        departamento.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Persona.objects.create(
            nombre = nombre,
            apellido = apellido,
            departamento = departamento
        )
        departamento = form.cleaned_data['departamento']
        return super(NuevoDepartamentoView, self).form_valid(form)
