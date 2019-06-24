# Django
from django.db import models

# Utils
from app.models.utils.models import HeezeClase


class Evento(HeezeClase, models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    imagen = models.CharField(max_length=100)

    precio_del_puesto = models.PositiveIntegerField(default=0)
    precio_ingreso = models.PositiveIntegerField(default=0)
    dinero_ganado = models.IntegerField(default=0)

    ya_ocurrio = models.BooleanField(default=False)
