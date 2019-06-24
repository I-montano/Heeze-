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

    template_name = 'login.html'