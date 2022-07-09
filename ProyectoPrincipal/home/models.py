from django.db import models

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo

class Manufacturer(models.Model):
    nombre = models.CharField(max_length=120)


class Product(models.Model): 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
