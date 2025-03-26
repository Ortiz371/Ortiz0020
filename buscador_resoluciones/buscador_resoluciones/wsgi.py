"""
WSGI config for buscador_resoluciones project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# Reemplaza ESTO:
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

# Por ESTO (versión moderna):
from whitenoise import WhiteNoise
application = WhiteNoise(application, root="staticfiles")
