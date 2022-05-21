from django import forms

class NuevoDepartamentoForm(forms.Form):
    """NuevoDepartamentoForm definition."""
    # TODO: Define form fields here
    nombre = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)