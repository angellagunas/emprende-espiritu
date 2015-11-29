# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from localflavor.mx.models import MXStateField, MXZipCodeField


class Galeria(models.Model):
    titulo = models.CharField(
        max_length=200
    )
    subtitulo = models.CharField(
        max_length=400
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
        upload_to='galeria/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name=_('Imagen')
    )

    description = models.TextField()

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
        verbose_name = u'Galeria'
        verbose_name_plural = u'Galeria'
