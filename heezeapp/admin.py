# Django
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from app.models.Usuario import Usuario
from app.models.Categoria import Categoria
from app.models.Comision import Comision
from app.models.Producto import Producto
from app.models.Venta import Venta
from app.models.Venta import Detalle_Venta
from app.models.Evento import Evento

# Utils
from app.models.utils.models import HeezeSettings
from app.models.utils.models import AcercaDeMi


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
    search_fields = ('pk', 'user')
    list_filter = ('creado_en', 'modificado_en', 'phone_number')

    fieldsets = (
        ('Usuario', {
            'fields': ('user', 'email')
        }),
        ('Metadata', {
            'fields': ('creado_en', 'modificado_en')
        }),
    )

    readonly_fields = ('creado_en', 'modificado_en')


class UsuarioInline(admin.StackedInline):
    """In-line Usuario."""
    model = Usuario
    can_delete = False
    verbose_name_plural = 'usuarios'


class UserAdmin(BaseUserAdmin):
    """Agrega el modelo de Usuario al base user admin."""
    inlines = (UsuarioInline, )
    list_display = ('username', 'email', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'id_producto')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('creado_en', 'modificado_en')


@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
    list_display = ('fecha_entrega', 'fue_abonada', 'fue_pagada',
                    'fue_enviada', 'fue_recibida',
                    'valoracion_final_de_usuario', 'id_usuario')
    search_fields = ('fecha_entrega', 'fue_abonada', 'fue_pagada',
                     'fue_enviada', 'fue_recibida',
                     'valoracion_final_de_usuario', 'id_usuario')
    list_filter = ('creado_en', 'modificado_en')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'precio', 'stock', 'tamano')
    search_fields = ('nombre', 'tipo', 'precio', 'stock', 'tamano')
    list_filter = ('creado_en', 'modificado_en', 'precio')


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'email', 'precio_total')
    search_fields = ('fecha', 'email', 'precio_total')
    list_filter = ('creado_en', 'modificado_en')


@admin.register(Detalle_Venta)
class Detalle_VentaVentaAdmin(admin.ModelAdmin):
    list_display = ('precio', 'id_producto', 'id_venta')
    search_fields = ('precio', 'id_producto', 'id_venta')
    list_filter = ('precio', 'creado_en', 'modificado_en')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'precio_del_puesto', 'precio_ingreso',
                    'dinero_ganado', 'ya_ocurrio')
    search_fields = ('nombre', 'fecha', 'ya_ocurrio')
    list_filter = ('nombre', 'fecha', 'ya_ocurrio')


@admin.register(AcercaDeMi)
class AcercaDeMiAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'descripcion')


@admin.register(HeezeSettings)
class HeezeSettingsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'oficina', 'twitter')
