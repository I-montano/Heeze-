# Django
from django.db import models

# Local
from .Singleton import SingletonModel


class HeezeSettings(SingletonModel):
    """Settings de la empresa Heeze.

    La clase HeezeSettings usa el patrón Singleton,
    ya que sólo exise una instancia de la empresa."""

    nombre = models.CharField(max_length=100, default="Heeze Ltd.")
    email = models.EmailField(default='heeze@gmail.com')
    oficina = models.CharField(max_length=100, default="Puente Alto, #3434")
    twitter = models.CharField(max_length=100,
                               default="https://twitter.com/heeze")
