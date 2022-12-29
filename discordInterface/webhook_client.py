from discord_webhook import DiscordWebhook
from discordInterface import webhook_message


class WebhookClient:

    def send_discord_message(self):
        webhook = DiscordWebhook(
            url='https://discordapp.com/api/webhooks/1044734812029718548/DM7bzMPkjlb4dmw1fFCwnCH'
                '-2v1fw9SMHHKDby2IEWXzVSInEFDXxnjkV6FpiciFtprd'
        )
        message = webhook_message.WebhookMessage()
        webhook.content = message.webhook_content
        webhook.add_embed(message.webhook_embed)
        return webhook.execute()
