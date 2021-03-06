from departamentos.models import Departamento
from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.habilidad


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fullname = models.CharField(
        'Nombre Completo',
        max_length=120,
        blank=True
    )
    puesto = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

        