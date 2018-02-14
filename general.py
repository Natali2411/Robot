import requests
import json
import os
import time, datetime

class General():
    def getConfig(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))
        with open(filename)as f:
            return json.load(f)

    def convertDateToTimestamp(self, dateTime):
        time.mktime(datetime.datetime.strptime(dateTime, "%d/%m/%Y").timetuple())

if __name__ == '__main__':
    obj = General()
    print(obj.getConfig()["gathering"]["base_api"])