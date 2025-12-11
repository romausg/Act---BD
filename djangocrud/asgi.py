"""
ASGI config for mi_grupo_personal project.

It exposes the ASGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_grupo_personal.settings')

application = get_asgi_application()