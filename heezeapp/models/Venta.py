# Django
from django.db import models

# Models
from .Usuario import Usuario
from .Producto import Producto

# Utils
from .utils.HeezeClase import HeezeClase
from .utils.Notificador import Notificador


class Venta(HeezeClase, models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.PositiveIntegerField()

    # Llave foránea
    id_usuario = models.ForeignKey(Usuario,
                                   on_delete=models.SET_NULL,
                                   null=True)


class Detalle_Venta(HeezeClase, models.Model):
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.PositiveIntegerField(default=0)

    # Llave foránea
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
