#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator


class AuthRedirectMixin(object):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse_lazy('archivos:lista_archivos'))
        else:
            return super(AuthRedirectMixin, self).get(self, request, *args,
                                                      **kwargs)


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('usuarios:login')))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)