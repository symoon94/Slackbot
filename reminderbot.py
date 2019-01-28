from time import sleep
from datetime import datetime
import config
from slackclient import SlackClient


token = config.token
BASE_URL = config.BASE_URL
notify_before = config.notify_before

client = SlackClient(token)

def current_time():
    now = datetime.now()
    return f"{now.hour}:{now.minute}"


def time_difference(from_time, to_time):
    global notify_before
    format= "%H:%M"
    t1 = datetime.strptime(from_time, format)
    t2 = datetime.strptime(to_time, format)
    difference = (((t1 - t2).seconds) // 60)
    return [True, difference] if difference in notify_before else [False, difference]


def send_notification(body):
    client.api_call("chat.postMessage",
                    channel=config.channel,
                    text=body,
                    username=config.username,
                    icon_emoji=':robot_face:')


now = current_time()

if client.rtm_connect() == True:
    print('Connected.')
    while True:
        for event, body in config.schedule.items():
            # check if the event body has time and message as key
            if 'time' not in body or 'message' not in body:
                raise Exception(f"The event '{event}' doesn't contain the 'time' or 'message' or both as key.")

            time = body.get('time').strip()
            print('time: \n', time, '\n now: ', now)
            notifiable = time_difference(time, now)
            print(notifiable)

            if notifiable[0]:
                msg = f"It's time to {body.get('message')}."
                send_notification(msg)

        sleep(1)


