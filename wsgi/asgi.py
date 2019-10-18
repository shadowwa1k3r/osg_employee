from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import os
import django
from channels.routing import get_default_application

import app.chat.urls

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            app.chat.urls.websocket_urlpatterns
        )
    ),
})