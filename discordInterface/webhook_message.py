import os
from discord_webhook import DiscordEmbed
from dotenv import load_dotenv

load_dotenv()


class WebhookMessage:

    def __init__(self):
        self.channel_url = os.getenv('CHANNEL_URL')
        self.channel_name = os.getenv('CHANNEL_NAME')

        self.webhook_content = self.channel_name + " went live on Twitch"
        self.webhook_embed = DiscordEmbed(
            title=self.channel_url,
            url=self.channel_url,
            color=6570404,
        )
