# Django
from django.db import models

# Models
from .Usuario import Usuario

# Utils
from heezeapp.models.utils.HeezeClase import HeezeClase


class Comision(HeezeClase, models.Model):
    nombre = models.CharField(max_length=100, default='')
    comentario = models.TextField(max_length=1000, default='')
    archivo = models.FileField(blank=True, upload_to='static/comisiones')

    fecha_entrega = models.DateTimeField()
    fue_abonada = models.BooleanField('fue abonada', default=False)
    fue_pagada = models.BooleanField('fue pagada', default=False)
    precio = models.PositiveIntegerField(default=0)
    fue_enviada = models.BooleanField('fue enviada', default=False)
    fue_recibida = models.BooleanField('fue recibida', default=False)

    valoracion_final_de_usuario = models.PositiveSmallIntegerField(default=5)

    id_usuario = models.ForeignKey(Usuario,
                                   on_delete=models.SET_NULL,
                                   null=True)
