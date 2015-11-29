# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import localflavor.mx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name='nombre')),
                ('activo', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'pa\xeds',
                'verbose_name_plural': 'paises',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.FileField(upload_to=b'photos/%Y/%m/%d', null=True, verbose_name='profile picture', blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, verbose_name='gender', choices=[(b'm', b'Hombre'), (b'f', b'Mujer')])),
                ('birthday', models.DateField(null=True, verbose_name='birthday', blank=True)),
                ('residence_state', localflavor.mx.models.MXStateField(blank=True, max_length=3, null=True, verbose_name='residence state', choices=[('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHH', 'Chihuahua'), ('CHP', 'Chiapas'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DIF', 'Distrito Federal'), ('DUR', 'Durango'), ('GRO', 'Guerrero'), ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de M\xe9xico'), ('MIC', 'Michoac\xe1n'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo Le\xf3n'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Quer\xe9taro'), ('ROO', 'Quintana Roo'), ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potos\xed'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucat\xe1n'), ('ZAC', 'Zacatecas')])),
                ('residence_zip_code', localflavor.mx.models.MXZipCodeField(max_length=5, null=True, verbose_name='residence ZIP code', blank=True)),
                ('residence_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='residence country', blank=True, to='perfil.Pais', null=True)),
                ('user', models.OneToOneField(related_name='profile', on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
