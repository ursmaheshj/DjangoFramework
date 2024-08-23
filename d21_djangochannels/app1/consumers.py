from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer 


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('---Websocket connected---',event)
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self,event):
        print('---Websocket received---',event)
        print('--Message received--:',event['text'])
        name = event['text']
        self.send({
            'type':'websocket.send',
            'text':f'Hi {name}'
        })
        print('--Reply send--')
    def websocket_disconnect(self,event):
        print('---Websocket disconnected---',event)
        raise StopConsumer #it wont show unnecessary [took too long to shut down and was killed.] everytime

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('---Websocket connected---',event)
        await self.send({
            'type':'websocket.accept'
        })
    async def websocket_receive(self,event):
        print('---Websocket received---',event)
        print('--Message received--:',event['text'])
        name = event['text']
        await self.send({
            'type':'websocket.send',
            'text':f'Hi {name}'
        })
        print('--Reply send--')
    async def websocket_disconnect(self,event):
        print('---Websocket disconnected---',event)
        raise StopConsumer



# import json
# from channels.generic.websocket import WebsocketConsumer
# class ChatConsumer(WebsocketConsumer):

#     def connect(self):
#         self.username = "Anonymous"
#         self.accept()
#         self.send(text_data="[Welcome %s!]" % self.username)

#     def receive(self, *, text_data):
#         if text_data.startswith("/name"):
#             self.username = text_data[5:].strip()
#             self.send(text_data="[set your username to %s]" % self.username)
#         else:
#             self.send(text_data=self.username + ": " + text_data)

#     def disconnect(self, message):
#         pass