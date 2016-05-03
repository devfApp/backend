from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = '(#o@k!5a1$)*jrfevryxict9#di2ujhyal9v3w+xc5=4hg$k)$'

ADMINS = (('Inaki', 'icaboalo@gmail.com'), )

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd2mjs5kgl18go2',
#         'USER': 'uteqffkoqsvrlh',
#         'PASSWORD': 'gFSY0nnebfpkSBtEksbvC9SwTc',
#         'HOST': 'ec2-54-83-22-48.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'