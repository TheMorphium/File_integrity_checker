import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('account_sid')
auth_code = os.getenv('auth_token')
assigned_did = os.getenv('from_num')



def send_message(send_number, body):
    client = Client(account_sid, auth_code)
    message = client.messages.create(body=body, from_=assigned_did, to=send_number)
    sid = message.sid
    return sid


def test_send():
    send_number = '+15627040239'
    body = 'This is a test text message'
    send_message(send_number, body)


