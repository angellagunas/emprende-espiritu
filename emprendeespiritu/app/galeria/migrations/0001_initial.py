# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=400)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('hora_creacion', models.TimeField(auto_now_add=True)),
                ('img', models.FileField(upload_to=b'galeria/%Y/%m/%d', null=True, verbose_name='Imagen', blank=True)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_creacion'],
                'verbose_name': 'Galeria',
                'verbose_name_plural': 'Galeria',
            },
        ),
    ]
