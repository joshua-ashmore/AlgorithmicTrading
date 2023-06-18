"""Telegram objects and functions."""

import requests


class Telegram:
    """Telegram objects containing relevant functions."""

    def send(self, text: str, bot_token: str, group_id: str):
        """Send message to telegram account."""
        group_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={group_id}&text={text}"
        return requests.post(url=group_message_url)
