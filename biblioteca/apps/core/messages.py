#!/usr/bin/python
# -*- coding: utf-8 -*-


regex_sentences = {
    'numbres_and_letters_special': '^[a-zA-Z0-9_áéíóúñ\s]*$',
    'numbres_and_letters': '^[a-zA-Z0-9]*$',
    'email': '^[\w.@+-]+$',
    'zip_code': '^[0-9\-]*$',
}


custom_error_messages = {
    'blank': 'El campo no puede estar en blanco',
    'invalid_login': 'Usuario o contraseña incorrectos',
    'inactive_account': 'Esta cuenta esta inactiva',
    'required': 'Este campo es requerido',
    'invalid': 'Ingresa un valor válido',
}