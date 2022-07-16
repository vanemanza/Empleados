from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50) # el primer parametro es como figurará en el admin de django
    codigo = models.IntegerField(null=True)
    area = models.CharField('Area', max_length=50, null=True, blank=True)

    def __str__(self):
        return f' {self.id} {self.nombre}'