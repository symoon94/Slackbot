from slackclient import SlackClient
from config import *

token = token

client = SlackClient(token = token)

call = client.api_call("channels.list")

result = call['ok']

print(result)

def send_message (channel_id, message):
    result = client.api_call(
        "chat.postMessage",
        channel = channel_id,
        text = message,
        username = username,
        icon_emoji = ':robot_face'
    )
    if not result['ok']:
        raise Exception(result['error'])



