# Django
from django.db import models


class Notificador(models.Model):
    """Notificador de la aplicación.

    La clase Notificador se encarga de notificar al administrador
    y al cliente luego de que el último realiza una compra o pago, 
    cumpliendo con el patrón de diseño 'Observer'.
    """
    mensaje = models.CharField(max_length=100, default="Heeze Ltd.")