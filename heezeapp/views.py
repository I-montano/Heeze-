# Django
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Models
from .models.Usuario import Usuario
from .models.utils.HeezeSettings import HeezeSettings

# Forms
from heezeapp.forms import SignupForm


def detalle_empresa(request):
    """Landing Page. Detalle de la empresa."""
    empresa = HeezeSettings.objects.all().filter(pk=1)
    return render(request, 'landing.html', context={'empresa': empresa[0]})


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'login.html',
                          {'error': 'Invalid username and password'})

    return render(request, 'login.html')


def signup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request=request,
                  template_name='signup.html',
                  context={'form': form})


# # Vistas de Usuario
# class LoginView(auth_views.LoginView):
#     """Login view."""

#     template_name = 'usuarios/login.html'

# class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
#     """Logout view."""

#     template_name = 'usuarios/logout.html'

# class SignupView(FormView):
#     """Users sign up view."""

#     template_name = 'usuarios/signup.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('heezeapp:login')

#     def form_valid(self, form):
#         """Guarda el dato del formulario."""
#         form.save()
#         return super().form_valid(form)

# class UpdateProfileView(LoginRequiredMixin, UpdateView):
#     """Vista de actualización de Usuario."""

#     template_name = 'actualizacion_usuario.html'
#     model = Usuario
#     fields = ['phone_number']

#     def get_object(self):
#         """Return user's profile."""
#         return self.request.user.usuario

#     def get_success_url(self):
#         """Return to user's profile."""
#         username = self.object.user.username
#         return reverse('heezeapp:detail', kwargs={'username': username})

# # Vistas de Empresa
# class LandingView(TemplateView):
#     model = HeezeSettings
#     template_name = 'landing.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(LandingView, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the team members
#         context['empresa'] = self.get_object().filter(pk=1)
#         return context

# # Utilidades (Comisiones)