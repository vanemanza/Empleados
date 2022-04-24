from django.contrib import admin

# Register your models here.
from .models import Persona, Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display =[
        'id',
        'nombre',
        'apellido',
        'puesto',
        'departamento',
        'nombre_completo'
    ]

    def nombre_completo(self, obj):
        return f'{obj.nombre} {obj.apellido}'

    #TODO 
    # agregar una funcion q me calcule la edad a partir de la fecha de nacimiento
    # agregar la fecha de nacimiento en el modelo   
    # 
    # TODO
    # VER SI ES NECESARIO INSTALAR CKEDITOR ? 

    search_fields = ('nombre', 'apellido')
    list_filter = ('departamento', 'habilidad', 'departamento')
    filter_horizontal = ('habilidad',)

admin.site.register(Persona, EmpleadoAdmin)