#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView

from biblioteca.apps.core.mixins import AuthRedirectMixin

from .forms import LoginForm


class LoginView(AuthRedirectMixin, FormView):
    template_name = 'usuarios/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('archivos:lista_archivos')

    def form_valid(self, form):
        login(self.request, form.user_cache)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data())


@login_required(login_url=reverse_lazy('usuarios:login'))
def logout_view(request):
    logout(request)
    return redirect('/')
