from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('---websocket connected---',event)
        print('---channel layer---',self.channel_layer) #default layer
        print('---channel name---',self.channel_name) #default name
        
        async_to_sync(self.channel_layer.group_add)('programmers',self.channel_name)  #adding channel to group 
        
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('---message received---',event)
        async_to_sync(self.channel_layer.group_send)('programmers',{
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self,event):
        print('---chat message---',event)
        self.send({
            'type':'websocket.send',
            'text': event['message']
        })
    def websocket_disconnect(self,event):
        print('---websocket disconnected---',event)
        print('---channel layer---',self.channel_layer)
        print('---channel name---',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)('programmers',self.channel_name)
        raise StopConsumer