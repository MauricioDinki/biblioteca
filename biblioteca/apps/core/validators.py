#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms

from .messages import custom_error_messages


def eval_blank(data):
    if str(data).isspace():
        raise forms.ValidationError(custom_error_messages['blank'],
                                    code='blank')
    return data

