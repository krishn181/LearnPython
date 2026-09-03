from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import asyncio,json
from asgiref.sync import async_to_sync
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connecting...")
        print("Channel layer...", self.channel_layer)
        # channel name
        print("channel name...",self.channel_name)
        # add channel to group and convert sync to async 
        async_to_sync(self.channel_layer.group_add)('programmers', #name of group as per choice
                                                    self.channel_name)
        self.send({
            "type":"websocket.accept"
        })

    def websocket_receive(self, event):
        print("Message Received...",event['text'])
        data = json.loads(event['text'])
        message = data['msg']
        print(message)
        async_to_sync(self.channel_layer.group_send)('programmers',{
            'type':'chat.message',
            'message':event['text'],
        })
        self.send({
            "type":"websocket.send"
        })

    def chat_message(self, event):
        print("Event.....",event['message'])
        data = json.loads(event['message'])
        msg=data['msg']
        print(msg)
        self.send({
                    "type":"websocket.send",
                    "text":event['message']
                })
        
    def websocket_disconnect(self, event):
        print("Channel layer...", self.channel_layer)
                # channel name
        print("channel name...",self.channel_name)
        #group discard
        async_to_sync(self.channel_layer.group_discard)('programmers', #name of group as per choice
                                                            self.channel_name)

        raise StopConsumer()