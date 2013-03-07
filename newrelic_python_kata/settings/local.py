"""Development settings and globals."""


from os.path import join, normpath

from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

INSTALLED_APPS += ('gunicorn',)


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': normpath(join(DJANGO_ROOT, 'default.db')),
        #'USER': '',
        #'PASSWORD': '',
        #'HOST': '',
        #'PORT': '',
    #}
#}
#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'ddcvf9qgum3id3',
        #'USER': 'fogurmzjhpoapl',
        #'PASSWORD': 'CaS7m7WiJbKoJKi58Bhkplf8wI',
        #'HOST': 'ec2-54-243-229-57.compute-1.amazonaws.com',
        #'PORT': '5432',
    #}
#}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION
