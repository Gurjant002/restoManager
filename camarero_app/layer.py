from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def enviar_pedido(pedido):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('pedidos', {
        'type': 'enviar_pedido',
        'pedido': pedido
    })