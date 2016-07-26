#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Permiso(models.Model):
    user = models.OneToOneField(
        User
    )
    embajador = models.BooleanField(
        default=False,
    )
    intern = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'

    def __unicode__(self):
        return unicode(self.user)
