import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import src.chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "messenger.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            src.chat.routing.websocket_urlpatterns
        )
    ),
})
