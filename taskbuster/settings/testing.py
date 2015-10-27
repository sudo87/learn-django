from .base import *
DEBUG = True
"""
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
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )