import Configuration
import requests
import data


def create_order():
    return requests.post(Configuration.URL + Configuration.METHOD, json=data.body)

def get_info(track):
    return requests.get(Configuration.URL + Configuration.ORDER + 'track')
