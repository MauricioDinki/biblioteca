#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$', view=views.ListaArchivos.as_view(), name='lista_archivos'),
]