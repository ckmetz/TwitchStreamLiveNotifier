import time

from twitchInterface import twitch_client
from discordInterface import webhook_client

discord_client = webhook_client.WebhookClient()
twitch_client = twitch_client.TwitchClient()

current_stream_id = 0
previous_stream_id = 1

while True:
    print('in while')
    print(current_stream_id)
    print(previous_stream_id)
    print(twitch_client.check_if_stream_is_live())
    print(not twitch_client.check_if_stream_is_live())
    if twitch_client.check_if_stream_is_live() and current_stream_id != previous_stream_id:
        print("and we're live!")
        current_stream_id = twitch_client.streamer.stream.id
        previous_stream_id = twitch_client.streamer.stream.id
        discord_client.send_discord_message()
    elif not twitch_client.check_if_stream_is_live():
        print('in else')
        current_stream_id = 0
        previous_stream_id = 1

    time.sleep(10)
