import django_filters as filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = filters.Charfield(lookup_expr='iexact')

    class Meta:
        models = Product 
        fields = ['price', 'release_date']

# como ModelForm se pueden anular los filtros o agregar otros usando la sintaxis declarativa?????
