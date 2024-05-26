from channels.generic.websocket import WebsocketConsumer
import json

from asgiref.sync import async_to_sync

class Test(WebsocketConsumer):
    def connect(self):
        print('Hola >',self.channel_name)
        self.GROUP_NAME = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME,
            self.channel_name
        )
        
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))