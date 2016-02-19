#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View

from biblioteca.apps.core.mixins import LoginRequiredMixin
from biblioteca.apps.categorias.models import Categoria

from .models import Archivo


class ListaArchivos(LoginRequiredMixin, View):
    template_name = 'archivos/lista_archivos.html'

    def get(self, request):
        archivos = Archivo.objects.all()
        categorias = Categoria.objects.all()

        context = {
            'archivos': archivos,
            'categorias': categorias,
        }

        return render(request, self.template_name, context)
