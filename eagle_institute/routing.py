# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import NotificationConsumer  # Import your WebSocket consumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/admin_notifications/", NotificationConsumer.as_asgi()),
        ])
    ),
})
