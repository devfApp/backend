from .base import * 
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2mjs5kgl18go2',
        'USER': 'uteqffkoqsvrlh',
        'PASSWORD': 'gFSY0nnebfpkSBtEksbvC9SwTc',
        'HOST': 'ec2-54-83-22-48.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'