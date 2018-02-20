import time
import json
import urllib
import hmac, hashlib, base64
import requests
from general import General

from urllib.parse import urlparse, urlencode
from urllib.request import Request, urlopen


class Authentication():
    def __init__(self, API_KEY, API_SECRET):
        self.API_KEY = API_KEY
        self.API_SECRET = bytearray(API_SECRET, encoding='utf-8')

    methods = {
        # private methods
        'createOrder': {'url': 'api/v3/order', 'method': 'POST', 'private': True},
        'testOrder': {'url': 'api/v3/order/test', 'method': 'POST', 'private': True},
        'orderInfo': {'url': 'api/v3/order', 'method': 'GET', 'private': True},
        'cancelOrder': {'url': 'api/v3/order', 'method': 'DELETE', 'private': True},
        'openOrders': {'url': 'api/v3/openOrders', 'method': 'GET', 'private': True},
        'allOrders': {'url': 'api/v3/allOrders', 'method': 'GET', 'private': True},
        'account': {'url': 'api/v3/account', 'method': 'GET', 'private': True},
        'myTrades': {'url': 'api/v3/myTrades', 'method': 'GET', 'private': True},
    }

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            kwargs.update(command=name)
            return self.call_api(**kwargs)

        return wrapper

    def call_api(self, **kwargs):

        command = kwargs.pop('command')
        api_url = 'https://api.binance.com/' + self.methods[command]['url']

        payload = kwargs
        headers = {}

        if self.methods[command]['private']:
            payload.update({'timestamp': int(time.time() * 1000)})
            sign = hmac.new(
                key=self.API_SECRET,
                msg=urllib.parse.urlencode(payload).encode('utf-8'),
                digestmod=hashlib.sha256
            ).hexdigest()
            payload.update({'signature': sign})
            #headers = {"X-MBX-APIKEY": self.API_KEY}
            h = hmac.new(key=bytearray(self.API_KEY, encoding='utf-8'), digestmod=hashlib.sha256).hexdigest()
            headers.update({"X-MBX-APIKEY": h})
        if self.methods[command]['method'] == 'GET':
            api_url += '?' + urllib.parse.urlencode(payload)

        res = {"method": self.methods[command]['method'], "api_url": api_url, "payload": payload, "headers": headers}
        #response = requests.request(method=self.methods[command]['method'], url=api_url, data=payload, headers=headers, verify=False)
        return res


if __name__ == '__main__':
    bot = Authentication(
        API_KEY='oIn05pd8WetMppBTPGwDqRqxoTkrQM9hNcA6kWWrZZHH4iqAEZinVzkHEAN4C03z',
        API_SECRET='NtMk5s34KVcC0VQ5OrzIPZpbRZLwM914FIXyeruY8bt4qaubHeuAfv56gavZXO4w'
    )
    print(bot.account())