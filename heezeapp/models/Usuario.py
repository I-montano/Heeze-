# Django
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Utils
from heezeapp.models.utils.HeezeClase import HeezeClase


class Usuario(HeezeClase, models.Model):
    """Modelo de Usuario."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        """Return username."""
        return self.user.username