from django.urls import re_path
from chat.controllers.websocket.consumers import ChatConsumer

websocket_urlpattners = [
    re_path(r'ws/socket-server/', ChatConsumer.as_asgi())
]