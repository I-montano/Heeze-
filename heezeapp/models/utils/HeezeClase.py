# Django
from django.db import models


class HeezeClase(models.Model):
    """Base de una clase Heeze.

    HeezeClase actúa como una clase abstracta que
    heredará al resto de la clases. Esta clase incluye los
    siguientes atributos:
        + creado_en (DateTime) = Fecha en la que fue creada
        + modificado_en (DateTime) = Última fecha en la que fue modificada

    HeezeClase busca proporcionar una interfaz de un modo más pythonico, 
    para así cumplir con el patrón Fecade.
    """

    creado_en = models.DateTimeField('creado en',
                                     auto_now_add=True,
                                     help_text="Fecha de creación.")
    modificado_en = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Última fecha de modificación.')

    class Meta:
        abstract = True

        get_latest_by = 'creado_en'
        ordering = ['-creado_en', '-modificado_en']