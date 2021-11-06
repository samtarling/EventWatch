import requests
import constants
from discord import Webhook, RequestsWebhookAdapter


def sendPlain(message: str):
    webhook = Webhook.from_url(
        constants.WEBHOOK,
        adapter=RequestsWebhookAdapter()
    )
    webhook.send(message)
