import requests


def get_tokens(url, body=None):
    return requests.post(url=url, headers={'Content-Type': 'application/json'}, json=body)


def send_post(url, access_token, body=None):
    return requests.post(url=url,
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token},
                         json=body)


def send_get(url, access_token, body=None):
    return requests.get(url=url,
                        headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token},
                        json=body)
