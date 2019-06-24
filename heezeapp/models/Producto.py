# Django
from django.db import models

# Utils
from app.models.utils.models import HeezeClase


class Producto(HeezeClase, models.Model):
    """Modelo de Producto."""
    nombre = models.CharField(max_length=100, default='')
    tipo = models.CharField(max_length=100)
    precio = models.PositiveIntegerField(blank=False, default=0)
    stock = models.PositiveIntegerField(blank=False)
    tamano = models.CharField(max_length=20, default='10cm x 10cm')
    imagen = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nombre
