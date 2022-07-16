from django.contrib import admin
from .models import Departamento
# Register your models here.


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo', 'area']

    search_fields = ('nombre', 'codigo', 'area' )
    list_filter = ('nombre', 'codigo', 'area')
 
admin.site.register(Departamento, DepartamentoAdmin)

