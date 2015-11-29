# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from localflavor.mx.models import MXStateField, MXZipCodeField


class Entrada(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name=_('Titulo')
    )
    fecha_creacion = models.DateField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True
    )
    hora_creacion = models.TimeField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True
    )
    img = models.FileField(
        upload_to='blog/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name=_('Imagen')
    )
    contenido = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return self.titulo

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name = u'Entrada'
        verbose_name_plural = u'Entradas'


class ComentarioBlog(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        verbose_name=_('Comentarios Blog')
    )

    entrada = models.ForeignKey(
        Entrada,
        on_delete=models.PROTECT
    )

    fecha_creacion = models.DateField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True
    )
    hora_creacion = models.TimeField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True
    )
    contenido = models.TextField()

    def __unicode__(self):
        return self.contenido


class LikeEntrada(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    entrada = models.ForeignKey(
        Entrada,
        on_delete=models.PROTECT
    )
