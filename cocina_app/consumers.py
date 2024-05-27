from channels.generic.websocket import AsyncWebsocketConsumer

import json

class PedidosConsumer(AsyncWebsocketConsumer):
  def connect(self):
    print("connect")
    self.accept()
    self.send(text_data=json.dumps({"message": "hello world"}))
  
  def receive(self, text_data=None):
    print("receive")
    text_data = json.loads(text_data)
    print(text_data)
    self.send(text_data)
  
  def disconnect(self, close_code):
    print("disconnect")
    self.close
