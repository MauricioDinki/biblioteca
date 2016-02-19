#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass