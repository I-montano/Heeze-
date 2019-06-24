# Django
from django import forms

# Models
from django.contrib.auth.models import User
from heezeapp.models.Usuario import Usuario


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70,
                                            widget=forms.PasswordInput())
    email = forms.CharField(min_length=6,
                            max_length=70,
                            widget=forms.EmailInput())

    def clean_username(self):
        """Username debe ser único."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El username ya existe.')
        return username

    def clean(self):
        """Verificar que la confirmación de la password coincida."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('La password no coincide.')

        return data

    def save(self):
        """Crear user y usuario"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        usuario = Usuario(user=user)
        usuario.save()
