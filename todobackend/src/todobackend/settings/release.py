from base import *
import os

if os.environ.get('DEBUG'):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
        'USER': os.environ.get('MYSQL_USER', 'root'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', '123456'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
    }
}

STATIC_ROOT = os.environ.get("STATIC_ROOT", '/var/www/todobackend/static')
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", '/var/www/todobackend/media')
