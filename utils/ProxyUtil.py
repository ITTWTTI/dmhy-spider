import requests
import re

base_url = 'http://127.0.0.1:5010/'


def get_proxy():
    return get_proxy_all().get('proxy')


def get_proxy_all():
    return requests.get(base_url + 'get').json()


def delete_proxy(proxy):
    requests.get(base_url + 'delete/?proxy={}'.format(proxy))


def pop_proxy_all():
    return requests.get(base_url + '/pop').json()


def pop_proxy():
    return pop_proxy_all().get('proxy')


def dict_proxy():
    proxy = get_proxy_all()
    return {
        'https': 'https://{}'.format(proxy.get('proxy')),
        'http': 'http://{}'.format(proxy.get('proxy'))
    }


def delete_dict_proxy(proxy):
    result = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})', proxy.get('http'))
    delete_proxy(result[0])
