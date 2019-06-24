# Django
from django import forms

# Models
from django.contrib.auth.models import User
from heezeapp.models.Usuario import Usuario


class SignupForm(forms.Form):
    """Sign up formulario."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70,
                                            widget=forms.PasswordInput())

    email = forms.CharField(min_length=6,
                            max_length=70,
                            widget=forms.EmailInput())

    def clean_username(self):
        """Username debe ser unico."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError(
                'El username ya se encuentra registrado.')
        return username

    def clean(self):
        """Verificador de confirmación de password."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las passwords no coinciden.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        usuario = Usuario(user=user)
        usuario.save()