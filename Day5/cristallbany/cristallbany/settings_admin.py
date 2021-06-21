from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django_diagram',
    'USER': 'django',
    'PASSWORD': 'admin',
    'HOST': '172.0.40.223',
    'PORT': 3306,
}
