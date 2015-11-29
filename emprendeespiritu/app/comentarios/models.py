# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from localflavor.mx.models import MXStateField, MXZipCodeField


class Comentario(models.Model):

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

    status = models.BooleanField(
        default=True
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return self.contenido

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name = u'Comentario'
        verbose_name_plural = u'Comentarios'
