#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

from biblioteca.apps.categorias.models import Categoria

from private_media.storages import PrivateMediaStorage


class Archivo(models.Model):
    archivo = models.FileField(
        blank=False,
        null=False,
        storage=PrivateMediaStorage(),
    )

    categoria = models.ForeignKey(
        Categoria,
        blank=False,
        null=False,
    )

    nombre = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __unicode__(self):
        return self.nombre
