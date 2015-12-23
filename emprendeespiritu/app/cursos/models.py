# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from localflavor.mx.models import MXStateField, MXZipCodeField


class Curso(models.Model):

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
        upload_to='curso/',
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

    @property
    def get_semanas(self):
        semanas = SemanaCurso.objects.filter(curso=self)
        return semanas

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name = u'Curso'
        verbose_name_plural = u'Cursos'

class SemanaCurso(models.Model):
    """semanas que tendra un curso"""
    curso = models.ForeignKey(
        Curso,
        verbose_name=_('curso'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    nombre = models.CharField(
        max_length=200,
        verbose_name=_('Semana del curso')
    )

    @property
    def get_archivos(self):
        archivos = ArchivoSemana.objects.filter(semana=self.id)
        return archivos

    def __unicode__(self):
        return "%s del curso %s"%(self.nombre, self.curso.nombre)

class ArchivoSemana(models.Model):
    """docstring for ArchivoSemana"""
    semana = models.ForeignKey(
        SemanaCurso,
        verbose_name=_('semana'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    archivo = models.FileField(
        upload_to='curso/archivos/',
        null=True,
        blank=True,
        verbose_name=_('Archivo')
    )

    def __unicode__(self):
        path = self.archivo.name
        filename = path.replace('curso/archivos/', '')
        return filename


class ComentarioCurso(models.Model):
    """docstring for ComentarioTaller"""
    curso = models.ForeignKey(
        Curso,
        verbose_name=_('curso'),
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
        verbose_name=_('Semana del curso')
    )

    fecha_creacion = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=False,
        auto_now_add=True
    )

    def __unicode__(self):
        return self.comentario

class LikeCurso(models.Model):
    """docstring for LikeTaller"""
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    curso = models.ForeignKey(
        Curso,
        verbose_name=_('curso'),
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )