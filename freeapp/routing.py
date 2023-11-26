from django.urls import re_path
from freeapp import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.DataConsumer.as_asgi()),
]
