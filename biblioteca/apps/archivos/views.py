#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View

from biblioteca.apps.core.mixins import LoginRequiredMixin
from biblioteca.apps.categorias.models import Categoria

from .models import Archivo, Link


class ListaArchivos(LoginRequiredMixin, View):
    template_name = 'archivos/lista_archivos.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        archivos = Archivo.objects.all()
        links = Link.objects.all()

        context = {
            'archivos': archivos,
            'links': links,
            'categorias_embajador': categorias.filter(embajador=True),
            'categorias_emma': categorias.filter(emma=True),
            'categorias_intern': categorias.filter(intern=True),
        }

        return render(request, self.template_name, context)
