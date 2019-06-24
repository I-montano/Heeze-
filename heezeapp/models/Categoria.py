# Django
from django.db import models

# Models
from .Producto import Producto

# Utils
from heezeapp.models.utils.HeezeClase import HeezeClase


class Categoria(HeezeClase, models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True)

    # Llave foránea
    id_producto = models.ForeignKey(Producto,
                                    on_delete=models.SET_NULL,
                                    null=True)

    def __str__(self):
        return self.nombre
