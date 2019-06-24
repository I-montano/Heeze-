# Generated by Django 2.2.2 on 2019-06-24 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcercaDeMi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Fanny Salazar', max_length=100)),
                ('descripcion', models.CharField(default='Vivo en puente alto con mi pololo Nachotes. Estudié Animación Digital en Santo Tomás y me dedico a vender mis diseños.', max_length=500)),
                ('edad', models.PositiveIntegerField(default=22)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('imagen', models.CharField(max_length=100)),
                ('precio_del_puesto', models.PositiveIntegerField(default=0)),
                ('precio_ingreso', models.PositiveIntegerField(default=0)),
                ('dinero_ganado', models.IntegerField(default=0)),
                ('ya_ocurrio', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeezeSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Heeze Ltd.', max_length=100)),
                ('email', models.EmailField(default='heeze@gmail.com', max_length=254)),
                ('oficina', models.CharField(default='Puente Alto, #3434', max_length=100)),
                ('twitter', models.CharField(default='https://twitter.com/heeze', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notificador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(default='Heeze Ltd.', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('stock', models.PositiveIntegerField()),
                ('tamano', models.CharField(default='10cm x 10cm', max_length=20)),
                ('imagen', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('precio_total', models.PositiveIntegerField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='heezeapp.Usuario')),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heezeapp.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='heezeapp.Venta')),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('fecha_entrega', models.DateTimeField()),
                ('fue_abonada', models.BooleanField(default=False, verbose_name='fue abonada')),
                ('fue_pagada', models.BooleanField(default=False, verbose_name='fue pagada')),
                ('precio', models.PositiveIntegerField(default=0)),
                ('fue_enviada', models.BooleanField(default=False, verbose_name='fue enviada')),
                ('fue_recibida', models.BooleanField(default=False, verbose_name='fue recibida')),
                ('valoracion_final_de_usuario', models.PositiveSmallIntegerField(default=5)),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='heezeapp.Usuario')),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creado_en', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación.', verbose_name='creado en')),
                ('modificado_en', models.DateTimeField(auto_now=True, help_text='Última fecha de modificación.', verbose_name='modified at')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=100)),
                ('id_producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='heezeapp.Producto')),
            ],
            options={
                'ordering': ['-creado_en', '-modificado_en'],
                'get_latest_by': 'creado_en',
                'abstract': False,
            },
        ),
    ]