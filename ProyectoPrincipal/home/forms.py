from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        fields = ('__all__')

        # usamos los widgets para personalizar los campos de un formulario -> dict
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingrese palabras con P',
                }
            )         

        }
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if not titulo.startswith("P"):
            raise forms.ValidationError('El título debe comenzar con la letra P mayúscula!!!!!!')
        return titulo    

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('La cantidad debe ser mayor a 10.')
        return cantidad        
