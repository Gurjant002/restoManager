from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/<pedidos>', PedidosConsumer.as_asgi()),
]