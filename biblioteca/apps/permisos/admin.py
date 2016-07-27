#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Permiso


@admin.register(Permiso)
class PermisoAdmin(admin.ModelAdmin):
    list_display = ('user', 'embajador', 'intern', 'emma')