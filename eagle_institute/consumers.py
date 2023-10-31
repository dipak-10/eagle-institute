import json
from channels.generic.websocket import AsyncWebsocketConsumer
from sms_gateway import send_sms_notification  # Import your SMS gateway integration function

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def send_notification(self, event):
        message = event['message']

        # Send an SMS notification using your SMS gateway integration
        recipient_number = '7096100823'  # Replace with the admin's mobile number
        send_sms_notification(recipient_number, message)

        await self.send(text_data=json.dumps({
            'message': message
        }))
