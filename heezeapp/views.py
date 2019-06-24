# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User

# Forms
from heezeapp.forms import SignupForm


# Create your views here.
class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'usuarios/login.html'


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'usuarios/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('heezeapp:login')

    def form_valid(self, form):
        """Guarda el dato del formulario."""
        form.save()
        return super().form_valid(form)