from django.shortcuts import render, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync  # Import the async_to_sync function


def admission(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        gender = request.POST.get('gender')
        age = request.POST.get('age')

        # Send a WebSocket notification to the admin
        channel_layer = get_channel_layer()

        async def send_notification():
            await channel_layer.group_add("admin_notifications", "notification_channel")
            await channel_layer.group_send("admin_notifications", {
                "type": "send_notification",
                "message": "New form submission received.",
            })

            async_to_sync(send_notification)()

        return redirect('/admission')
    return render(request, 'admission.html')