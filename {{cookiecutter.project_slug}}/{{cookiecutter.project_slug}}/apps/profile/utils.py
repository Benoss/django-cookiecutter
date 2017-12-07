from django.conf import settings
import requests

url_api = "https://api.mailgun.net/v3/routes"
my_auth = ("api", settings.MAILGUN_API_KEY)


def create_rule_forward(forward_email=None, from_email=None, description=None, priority=100):
    action = []
    for email in forward_email:
        if email != "":
            action.append(f'forward("{email}")')
    return {
        "priority": priority,
        "description": description,
        "expression": f'match_recipient("{from_email}")',
        "action": action
    }


def create_route(**kwargs):
    data = create_rule_forward(**kwargs)
    ret = requests.post(url_api, auth=my_auth, data=data)
    answer = ret.json()
    return answer['route']['id']


def update_route(rule_id, **kwargs):
    data = create_rule_forward(**kwargs)
    ret = requests.put(f'{url_api}/{rule_id}', auth=my_auth, data=data)
