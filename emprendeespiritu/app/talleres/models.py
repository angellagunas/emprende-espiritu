# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from localflavor.mx.models import MXStateField, MXZipCodeField

class Taller(models.Model):

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
    
    nombre = models.CharField(
        max_length=200
    )

    descripcion = models.TextField()

    status = models.BooleanField(
        default=True
    )

    img = models.FileField(
        upload_to='taller/',
        null=True,
        blank=True,
        verbose_name=_('Imagen')
    )

    precio = models.DecimalField(
        default=0,
        blank=False,
        null=False,
        max_digits=8,
        decimal_places=2
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name = u'Taller'
        verbose_name_plural = u'Talleres'

class SemanaTaller(models.Model):
    """semanas que tendra un taller"""
    taller = models.ForeignKey(
        Taller,
        verbose_name=_('taller'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    nombre = models.CharField(
        max_length=200,
        verbose_name=_('Semana del taller')
    )

    def __unicode__(self):
        return "%s del taller %s"%(self.nombre, self.taller.nombre)

class ArchivoSemana(models.Model):
    """docstring for ArchivoSemana"""
    semana = models.ForeignKey(
        SemanaTaller,
        verbose_name=_('semana'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    archivo = models.FileField(
        upload_to='taller/archivos/',
        null=True,
        blank=True,
        verbose_name=_('Archivo')
    )

    def __unicode__(self):
        path = self.archivo.name
        filename = path.replace('taller/archivos/', '')
        return filename

class ComentarioTaller(models.Model):
    """docstring for ComentarioTaller"""
    taller = models.ForeignKey(
        Taller,
        verbose_name=_('taller'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    comentario = models.CharField(
        max_length=200,
        verbose_name=_('Semana del taller')
    )

    fecha_creacion = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True
    )

    def __unicode__(self):
        return self.comentario

class LikeTaller(models.Model):
    """docstring for LikeTaller"""
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    taller = models.ForeignKey(
        Taller,
        verbose_name=_('taller'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

        