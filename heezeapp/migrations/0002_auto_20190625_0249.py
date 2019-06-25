# Generated by Django 2.2.2 on 2019-06-25 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heezeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comision',
            name='archivo',
            field=models.FileField(blank=True, upload_to='static/comisiones'),
        ),
        migrations.AddField(
            model_name='comision',
            name='comentario',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='comision',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
    ]