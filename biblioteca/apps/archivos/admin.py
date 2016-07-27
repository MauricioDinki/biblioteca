#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Archivo, Link


@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')