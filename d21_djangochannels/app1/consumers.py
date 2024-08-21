from channels.consumer import SyncConsumer,AsyncConsumer

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('---Websocket connected---')
    def websocket_receive(self,event):
        print('---Websocket received---')
    def websocket_disconnect(self,event):
        print('---Websocket disconnected---')

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('---Websocket connected---')
    async def websocket_receive(self,event):
        print('---Websocket received---')
    async def websocket_disconnect(self,event):
        print('---Websocket disconnected---')