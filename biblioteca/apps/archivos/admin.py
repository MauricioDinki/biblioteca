#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Archivo


@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    pass