import os
import site
import sys

python_version = sys.version_info
python_lib_folder = f'/env/lib/python{sys.version_info[0]}.{sys.version_info[1]}/site-packages/'

site.addsitedir(os.curdir + python_lib_folder)

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('account_sid')
auth_code = os.getenv('auth_token')
assigned_did = os.getenv('from_num')

messages_sent = 0



def send_message(send_number, body):
    return
    #client = Client(account_sid, auth_code)
    #message = client.messages.create(body=body, from_=assigned_did, to=send_number)
    #sid = message.sid
    #return sid


def test_send():
    send_number = '+15627040239'
    body = 'This is a test text message'
    send_message(send_number, body)


