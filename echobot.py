from time import sleep
from slackclient import SlackClient
import os

from config import *

token = token
client = SlackClient(token)

if client.rtm_connect() == True:
    print('Connected.')
    while True:
        response = client.rtm_read()
        print(response)
        for part in response:
            if part['type'] == 'message':
                if 'user' in part:
                    result = client.api_call(
                        "chat.postMessage",
                        channel=part['channel'],
                        text=part['text'],
                        username=username,
                        icon_emoji=':robot_face:')
        sleep(1)
else:
  print('Connection Failed, invalid token?')



