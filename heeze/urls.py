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
    path('signup/', view=views.signup_view, name='signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
