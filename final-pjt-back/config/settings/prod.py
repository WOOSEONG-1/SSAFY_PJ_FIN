from .base import *
import os
import environ

ALLOWED_HOSTS = ['mypjt.xyz', '127.0.0.1']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')
GPT_KEY = env('GPT_KEY')
FIN_KEY = env('FIN_KEY')


# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': env('DB_NAME'),
#        'USER': env('DB_USER'),
#        'PASSWORD': env('DB_PASSWORD'),
#        'HOST': env('DB_HOST'),
#        'PORT': '5432',
#    }
# }
