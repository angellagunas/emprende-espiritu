# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeEntrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='likeblog',
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='likeblog',
            name='user',
        ),
        migrations.AlterField(
            model_name='comentarioblog',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comentarioblog',
            name='hora_creacion',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='hora_creacion',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
        migrations.DeleteModel(
            name='LikeBlog',
        ),
        migrations.AddField(
            model_name='likeentrada',
            name='entrada',
            field=models.ForeignKey(to='blog.Entrada', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='likeentrada',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
