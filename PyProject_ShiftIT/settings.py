# -*- coding: utf-8 -*-
# Django settings for PyProject_ShiftIT project.

import os
import sys

PROJECT_ROOT_PATH= os.path.dirname(os.path.abspath(__file__))

LOCAL= True
DEBUG = False
EMAIL = True
TEMPLATE_DEBUG = DEBUG

try:
    if 'test' in sys.argv:
        from test_settings import *
    else:
        from local_settings import *
except ImportError:
    pass

ADMINS = (
     ('Shift it', 'suporte@shiftit.com.br'),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

LANGUAGES = (('pt-br', u'Português'),
             ('en', u'Inglês'))

SITE_ID = 1

LOCALE_DIR = '/tmp/'

FALLBACK_LANGUAGES = {
    'pt-br':[],
    'en':['pt-br'],
}

MSGID_LANGUAGE = 'pt-br'
             
SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '8lu*6g0lg)9z!ba+a$ehk)xt)x%rxgb$i1&amp'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'autenticacao.admin_locale.AdminLocaleURLMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'PyProject_ShiftIT.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'flatpages',
    'comunicacao',
    'autenticacao',
    'bugtracker',
    'kronos',
    'skwissh',
    'south',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

