from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'manniit',
        'PASSWORD': 'manniit',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}