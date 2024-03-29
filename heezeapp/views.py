# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Models
from .models.Usuario import Usuario
from .models.Evento import Evento
from .models.Producto import Producto
from .models.Comision import Comision
from .models.utils.HeezeSettings import HeezeSettings
from .models.utils.AcercaDeMi import AcercaDeMi

# Forms
from .forms import SignupForm, ComisionForm


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
            return redirect('landing')
        else:
            return render(request, 'usuarios/login.html',
                          {'error': 'Password o username inválido.'})

    return render(request, 'usuarios/login.html')


@login_required
def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect('landing')


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


def acerca_de_mi_view(request):
    """Acerca de mi view."""
    fanny = AcercaDeMi.objects.all().filter(pk=1)
    return render(request, 'acerca_de_mi.html', context={'fanny': fanny[0]})


def mis_disenos_view(request):
    """Mis diseños view."""
    disenos = Producto.objects.all().order_by('-creado_en')
    return render(request, 'mis_disenos.html', context={'disenos': disenos})


def proximos_eventos_view(request):
    """Próximos eventos view."""
    eventos = Evento.objects.all().order_by('-creado_en')
    return render(request,
                  'proximos_eventos.html',
                  context={'eventos': eventos})


@login_required
def comisiones_view(request):
    """Comisiones view."""
    comisiones_pendientes = Comision.objects.filter().order_by('-creado_en')
    if not comisiones_pendientes:
        return render(request, 'comision.html',
                      {'comisiones_pendientes': comisiones_pendientes})
    return render(request, 'comision_pendiente.html',
                  {'comisiones_pendientes': comisiones_pendientes})


@login_required
def carrito_de_compras_view(request):
    compras = []
    return render(request, 'carrito_de_compras.html', {'compras': compras})


def realizar_comision_view(request):
    """Formulario de Comision."""
    if request.method == 'POST':
        form = ComisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comision_pendiente.html')
    else:
        form = ComisionForm()
    return render(request=request,
                  template_name='comision_pendiente.html',
                  context={'comision_pendiente': form})