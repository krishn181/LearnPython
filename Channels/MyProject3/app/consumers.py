from channels.consumer import AsyncConsumer, SyncConsumer
from channels.exceptions import StopConsumer
import json
from .models import Chat, Group
from channels.auth import AuthMiddlewareStack
from asgiref.sync import async_to_sync
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connecting...")
        print("Channel layer...", self.channel_layer)
        # channel name
        print("channel name...",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['gorupName']

        # add channel to group and convert sync to async 
        async_to_sync(self.channel_layer.group_add)(self.group_name, #name of group as per choice
                                                    self.channel_name)
        self.send({
            "type":"websocket.accept"
        })

    def websocket_receive(self, event):
        print("Message Received...", event['text'])
        data = json.loads(event['text'])
        message = data['msg']

        print(message)

        self.group_name = self.scope['url_route']['kwargs']['gorupName']

        print("Group name", self.group_name)
        try:
            group = Group.objects.get(name=self.group_name)
        except Group.DoesNotExist:
            pass
        if self.scope['user'].is_authenticated:
            chat = Chat(content = message, group = group)
            chat.save()
            async_to_sync(self.channel_layer.group_send)(
            self.group_name,
                {
                    'type': 'chat.message',
                    'message': event['text'],
                }        )
        else:
            self.send({
                'type':'websocket.send',
                'text':json.dumps({"msg":"login required"}),
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
        self.group_name = self.scope['url_route']['kwargs']['gorupName']
        async_to_sync(self.channel_layer.group_discard)(self.group_name, #name of group as per choice
                                                            self.channel_name)

        raise StopConsumer()