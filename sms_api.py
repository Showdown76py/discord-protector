from asyncio.constants import _SendfileMode
from twilio.rest import Client
import os, json
from dotenv import load_dotenv
load_dotenv()

TESTING=False
ACCOUNTID='unknown'
with open('config.json','r')as f:
    if json.load(f)['sms']:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

class PrebuiltMessages:
    PHISHING = 'Your Discord account sends phishing links similar to Discord or Steam Community domains.'
    DM_ALL = 'Your Discord account is sending a lot of Discord invites in different channels/user DMs!'
    CONNECTION_LOST = 'INVALID TOKEN. Your token was regenerated because your password or e-mail has changed. Please update your token.'


def sendSMS(message):
    with open('config.json','r')as f:
        if json.load(f)['sms']:
            if not TESTING:
                message = client.messages.create(
                    body=f"Univers Account Protection Alert\nACCOUNT: {ACCOUNTID}\n\nContinuous monitoring has detected unusual activities.\n\n{message}\n\nIT IS RECOMMENDED THAT YOU CHANGE YOUR PASSWORD IMMEDIATELY.\nhttps://discord.com/login",
                    to=os.environ['PHONE_NUMBER'],
                    from_='UnivrsPrtct'
                )
