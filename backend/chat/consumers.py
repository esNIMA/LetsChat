import json
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework_simplejwt.tokens import AccessToken
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from urllib.parse import parse_qs

# Dictionary to track active connections per user
connected_users = {}

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat_room'

        # Decode and parse the query string to extract parameters
        query_string = self.scope['query_string'].decode('utf-8')
        params = parse_qs(query_string)

        # Extract the token from the parsed query string
        token = params.get('token', [None])[0]

        try:
            # Check if the token is present
            if token is None:
                raise ValueError("Token is missing")

            # Verify the JWT token
            access_token = AccessToken(token)
            user = await self.get_user(access_token['user_id'])
            self.scope['user'] = user

            # Check if the user is already connected in another tab
            if user.username in connected_users:
                # Close the existing WebSocket connection for this user
                old_channel_name = connected_users[user.username]
                await self.close_existing_connection(old_channel_name)

            # Add the new connection to the connected users list
            connected_users[user.username] = self.channel_name

            # Add the user to the chat room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            # Accept the WebSocket connection
            await self.accept()
        except Exception as e:
            print("Token verification or connection failed:", e)
            await self.close()

    async def disconnect(self, close_code):
        # Remove the user from the connected users list on disconnect
        user = self.scope.get('user')
        if user and user.username in connected_users:
            del connected_users[user.username]

        # Remove the user from the chat room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.scope['user'].username

        # Send the message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        # Send the received message to WebSocket clients
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
        }))

    @database_sync_to_async
    def get_user(self, user_id):
        # Fetch user from the database by user_id
        return User.objects.get(id=user_id)

    async def close_existing_connection(self, old_channel_name):
        """
        Close the existing WebSocket connection for the user.
        """
        try:
            # Send a WebSocket close message to the old connection
            await self.channel_layer.send(old_channel_name, {
                'type': 'websocket.close',
            })
        except Exception as e:
            print(f"Error closing the old connection: {e}")
