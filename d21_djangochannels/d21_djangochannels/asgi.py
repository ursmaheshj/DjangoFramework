"""
ASGI config for d21_djangochannels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from d21_djangochannels.routings import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd21_djangochannels.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': URLRouter(ws_urlpatterns)
})
