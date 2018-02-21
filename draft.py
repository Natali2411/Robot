import requests
import urllib
import json
import hashlib
import hmac
from collections import OrderedDict
from urllib.parse import urlparse, urlencode

server = "api.livecoin.net"
method = "/exchange/client_orders"
api_key = "gJx7Wa7qXkPtmTAaK3ADCtr6m5rCYYMy"
secret_key = bytearray("8eLps29wsXszNyEhOl9w8dxsOsM2lTzg", encoding="utf-8")

data = OrderedDict([('currencyPair', 'BTC/EUR')])

encoded_data = urllib.parse.urlencode(data).encode('utf-8')

sign = hmac.new(secret_key, msg=encoded_data, digestmod=hashlib.sha256).hexdigest().upper()

headers = {"Api-key": api_key, "Sign": sign}

requests.request("GET", method + '?' + encoded_data, '', headers)

print (data)
