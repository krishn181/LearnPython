from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
import asyncio, json
from time import sleep
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket is connect..",event)
        self.send({
            "type":"websocket.accept"
        })
    def websocket_receive(self, event):
        print("Websocket is recieve..",event)
        print(event['text'])
        self.send({
            "type":"websocket.send",
            "text": "Message send to client from server",
        })
    def websocket_disconnect(self, event):
        print("Websocket is disconnect..",event)
        raise StopConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket is connect..",event)
        await self.send({
            "type":"websocket.accept"
        })
    async def websocket_receive(self, event):
        print("Websocket is recieve..",event)
        print(event['text'])
        for i in range(10):
            await self.send({
                "type":"websocket.send",
                "text": json.dumps({"count":i})     #str(i),
                })
            await asyncio.sleep(1)
            
    async def websocket_disconnect(self, event):
        print("Websocket is disconnect..",event)
        raise StopConsumer