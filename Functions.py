import Configuration
import requests

import data


def create_order():
    return requests.post(Configuration.URL + Configuration.METHOD, json=data.body)
response = create_order()
z = response.json()['track']


def get_info():
    return requests.get(Configuration.URL + Configuration.ORDER + "?t=" + 'z')
otvet = get_info()

