# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from heezeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.detalle_empresa, name='landing'),
    path('login/', view=views.login_view, name='login'),
    path('logout/', view=views.logout_view, name='logout'),
    path('signup/', view=views.signup_view, name='signup'),
    path('acerca_de_mi/', view=views.acerca_de_mi_view, name='acerca_de_mi'),
    path('mis_disenos/', view=views.mis_disenos_view, name='mis_disenos'),
    path('comisiones/', view=views.comisiones_view, name='comisiones'),
    path('comision_pendiente/',
         view=views.comisiones_view,
         name='comision_pendiente'),
    path('proximos_eventos/',
         view=views.proximos_eventos_view,
         name='proximos_eventos'),
    path('carrito_de_compras/',
         view=views.carrito_de_compras_view,
         name='carrito'),
    path('realizar_comision/',
         view=views.realizar_comision_view,
         name='realizar_comision'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
