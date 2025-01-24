from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def send_Text(number, className, section):
    account_sid = os.environ.get("ACCOUNT_SID")
    auth_token = os.environ.get("AUTH_TOKEN")
    print(auth_token, account_sid)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=os.environ.get("NUMBER_FROM"),
        body=f'A spot opened up for {className}, section {section}.',
        to=number#string
    )
    print(message.sid)
