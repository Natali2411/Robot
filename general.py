import requests, json, os, datetime
import time, os, hmac, requests, hashlib

class General():
    def getConfig(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))
        with open(filename)as f:
            return json.load(f)

    def convertDateToTimestamp(self, dateTime, template="%Y/%m/%d %H:%M:%S"):
        if template == "%Y/%m/%d %H:%M:%S":
            dt = time.mktime(datetime.datetime.strptime(dateTime, template).timetuple())
        return dt

    def makeAuthentication(self):
        api = General().getConfig()["gathering"]["base_api"] + '/api/v3/openOrders/'
        body = ''
        nonce = int(time.time() * 1e6)
        API_SECRET = "" #secret
        ACCESS_KEY = "" #key
        message = str(nonce) + api + ('' if body is None else body)
        signature = hmac.new(API_SECRET, message, hashlib.sha256).hexdigest()
        # Include the signature in the headers
        headers = {
            'ACCESS_KEY': ACCESS_KEY,
            'ACCESS_SIGNATURE': signature,
            'ACCESS_NONCE': nonce,
            'Accept': 'application/json',
            'Content-Type': 'application/json'  # Only for POST requests
        }
        return api

if __name__ == '__main__':
    obj = General()
    print(obj.makeAuthentication())