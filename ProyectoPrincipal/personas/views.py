from django.shortcuts import render
from .models import Persona
# Create your views here.
def persona(request):
    personas = Persona.objects.all()
    contexto = {
        'persona':personas
    }
    return render(request, 'persona.html', contexto)