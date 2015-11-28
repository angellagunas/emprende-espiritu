# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from localflavor.mx.models import MXStateField, MXZipCodeField


class Pais(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=u'nombre'
    )
    activo = models.BooleanField(
        default=True,
        verbose_name=u'activo'
    )

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = u'país'
        verbose_name_plural = u'paises'


class UserProfile(models.Model):
    # Basic user information
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='profile',
        verbose_name=_('user')
    )
    picture = models.FileField(
        upload_to='perfil/%Y/%m/%d',
        null=True, blank=True,
        verbose_name=_('profile picture')
    )
    gender = models.CharField(
        max_length=1,
        choices=(('m', 'Hombre'), ('f', 'Mujer')),
        null=True, blank=True,
        verbose_name=_('gender')
    )
    birthday = models.DateField(
        null=True, blank=True,
        verbose_name=_('birthday')
    )
    residence_country = models.ForeignKey(
        Pais,
        on_delete=models.PROTECT,
        null=True, blank=True,
        verbose_name=_('residence country')
    )
    residence_state = MXStateField(
        null=True, blank=True,
        verbose_name=_('residence state')
    )
    residence_zip_code = MXZipCodeField(
        null=True, blank=True,
        verbose_name=_('residence ZIP code')
    )
    status = models.BooleanField(
        default=True
    )
