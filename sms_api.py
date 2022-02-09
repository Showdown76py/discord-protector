from asyncio.constants import _SendfileMode
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

TESTING=False

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

class PrebuiltMessages:
    PHISHING = 'Your Discord account sends phishing links similar to Discord or Steam Community domains.'
    DM_ALL = 'Your Discord account is sending a lot of Discord invites in different channels/user DMs!'


def sendSMS(message):
    print('Sending SMS...')
    if not TESTING:
        message = client.messages.create(
            body=f"Univers Account Protection Alert\nContinuous monitoring has detected unusual activities.\n\n{message}\n\nIT IS RECOMMENDED THAT YOU CHANGE YOUR PASSWORD IMMEDIATELY.\nhttps://discord.com/login",
            to=os.environ['PHONE_NUMBER'],
            from_='UnivrsPrtct'
        )
    print(f"Univers Account Protection Alert\nContinuous monitoring has detected unusual activities.\n\n{message}\n\nIT IS RECOMMENDED THAT YOU CHANGE YOUR PASSWORD IMMEDIATELY.\nhttps://discord.com/login")
    print('Sent!')
