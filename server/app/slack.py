import requests
import json
import settings as conf


def post_message_to_slack(text, blocks=None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': conf.slack_token,
        'channel': conf.slack_channel,
        'text': text,
        'icon_url': conf.slack_icon_url,
        'username': conf.slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
