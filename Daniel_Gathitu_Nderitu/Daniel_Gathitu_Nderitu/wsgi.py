"""
WSGI config for Daniel_Gathitu_Nderitu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Daniel_Gathitu_Nderitu.settings')

application = get_wsgi_application()
