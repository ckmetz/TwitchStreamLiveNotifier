import twitch
import os
from dotenv import load_dotenv

load_dotenv()


class TwitchClient:
    client_id = os.getenv('TWITCH_CLIENT_ID')
    secret = os.getenv('TWITCH_SECRET')
    streamer_name = os.getenv('TWITCH_USER')

    # Helix API with caching enabled
    helix = twitch.Helix(client_id=client_id, client_secret=secret, use_cache=True)

    streamer = helix.user(streamer_name)

    def check_if_stream_is_live(self):
        if self.streamer.is_live:
            return True

        return False
