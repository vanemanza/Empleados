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
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fullname = models.CharField(
        'Nombre Completo',
        max_length=120,
        blank=True
    )
    puesto = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='persona', blank=True, null=True)
    habilidad = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

        