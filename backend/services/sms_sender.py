from twilio.rest import Client

def send_sms(to, body):
    client = Client('your_twilio_sid', 'your_twilio_auth_token')
    message = client.messages.create(
        body=body,
        from_='your_twilio_phone_number',
        to=to
    )
