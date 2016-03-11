"""
WSGI config for djDevf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# for local use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djDevf.settings.local")

#for default use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djDevf.settings")


application = get_wsgi_application()
