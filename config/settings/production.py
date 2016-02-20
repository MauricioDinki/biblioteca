#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Production settings
- Run in production mode
- Use Amazon's S3 for storing static files
"""
from .base import *  # noqa

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = [".miemma.com"]

# DATABASE
# -----------------------------------------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

# STORAGE CONFIGURATION
# -----------------------------------------------------------------------------
INSTALLED_APPS += (
    'storages',
)

# STATIC CONFIGURATION
# -----------------------------------------------------------------------------

# Amazon s3 configuration
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

# static

# STATIC_URL = "https://%s/" % env("AWS_BUCKET_URL", None)

# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_ROOT = str(ROOT_DIR('staticfiles'))

STATIC_URL = '/static/'

# MEDIA CONFIGURATION
# -----------------------------------------------------------------------------
PRIVATE_MEDIA_ROOT = str(PROJECT_DIR('media/private'))

PRIVATE_MEDIA_URL = 'media/private/'

PRIVATE_MEDIA_SERVER = 'private_media.servers.DefaultServer'

PRIVATE_MEDIA_PERMISSIONS = 'biblioteca.apps.core.permissions.LoginPermission'

MEDIA_ROOT = str(PROJECT_DIR('media/public'))

MEDIA_URL = 'media/public/'
