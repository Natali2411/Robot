import requests, json, os, datetime
import time, os, hmac, requests, hashlib, urllib
from urllib.parse import urlparse, urlencode
from urllib.request import Request, urlopen

class General():
    def getConfig(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))
        with open(filename)as f:
            return json.load(f)

    def convertDateToTimestamp(self, dateTime, template="%Y/%m/%d %H:%M:%S"):
        if template == "%Y/%m/%d %H:%M:%S":
            dt = time.mktime(datetime.datetime.strptime(dateTime, template).timetuple())
        return dt

if __name__ == '__main__':
    obj = General()
