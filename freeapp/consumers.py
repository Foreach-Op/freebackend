import asyncio
import channels.exceptions
from django.core import serializers
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import timedelta
import json


class DataConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = {
            "DataLock": asyncio.Lock(),
        }

    async def connect(self):
        # user = self.scope["user"]
        self.group_name = "job-data"
        print(self.group_name)
        print(self.channel_name)

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def websocket_receive(self, event):
        pass

    async def send_data(self, signal_data):
        pass

    async def websocket_disconnect(self, event):
        await self.close()
        raise channels.exceptions.StopConsumer
