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
            name='ComentarioBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateField()),
                ('hora_creacion', models.TimeField()),
                ('contenido', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Comentarios Blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateField()),
                ('hora_creacion', models.TimeField()),
                ('img', models.FileField(upload_to=b'blog/%Y/%m/%d', null=True, verbose_name='Imagen', blank=True)),
                ('contenido', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_creacion'],
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
        ),
        migrations.CreateModel(
            name='LikeBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Like', to='blog.Entrada')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Comentarios Blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
