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
            name='Taller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('hora_creacion', models.TimeField(auto_now_add=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('img', models.FileField(upload_to=b'blog/%Y/%m/%d', null=True, verbose_name='Imagen', blank=True)),
                ('precio', models.DecimalField(default=0, max_digits=8, decimal_places=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_creacion'],
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
        ),
    ]
