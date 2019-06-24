# Django
from django.db import models

# Local
from .Singleton import SingletonModel


class AcercaDeMi(SingletonModel):
    """Acerca de mi contiene la información de Fanny desplegada en la página
    '/acerca-de-mi/'.

    Dado que la información no cambiará con demasiada frecuencia y no se 
    requieren diferentes instancias de esta, también se usa un patrón
    'Singleton'
    """
    nombre = models.CharField(max_length=100, default="Fanny Salazar")
    descripcion = models.CharField(
        max_length=500,
        default="Vivo en puente alto con mi pololo Nachotes. Estudié Animación "
        + "Digital en Santo Tomás y me dedico a vender mis diseños.")
    edad = models.PositiveIntegerField(default=22)