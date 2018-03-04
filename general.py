import requests, json, os, datetime
import time, os, hmac, requests, hashlib, urllib
from urllib.parse import urlparse, urlencode
from urllib.request import Request, urlopen
import datetime


class General():
    def getConfig(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))
        with open(filename)as f:
            return json.load(f)

    def convertDateToTimestamp(self, dateTime, template="%Y/%m/%d %H:%M:%S"):
        if template == "%Y/%m/%d %H:%M:%S":
            dt = datetime.datetime.strptime(dateTime, template).timestamp() * 1000
        return dt

    def getDateTimeCurrent(self):
        return str(datetime.datetime.now())

    def getCurrentTimestamp(self):
        return int(time.time() * 1000)

    def encodeParams(self, paramVal):
        params = {}
        param = hmac.new(
            key=bytearray(str(paramVal), encoding='utf-8'),
            msg=urllib.parse.urlencode(params).encode('utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()
        params.update({"param": param})
        return params["param"]

    def saveDataInFile(self, data):
        file = open("currency.txt", "a")
        file.write(str(data))
        file.close()
        return 'yes'



if __name__ == '__main__':
    obj = General()
    #print(obj.convertDateToTimestamp('2019/02/18 18:35:50'))
    print(obj.encodeParams('LTCETH'))
