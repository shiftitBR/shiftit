
from django.conf.global_settings import *

import os

PROJECT_ROOT_PATH= os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_URL= 'http://localhost:8000'

LOCAL = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',                                                          
    }
}

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'shift'
EMAIL_HOST_PASSWORD = 'shiftit@051011'
EMAIL_SUBJECT_PREFIX = '[FreelaTI.com]'