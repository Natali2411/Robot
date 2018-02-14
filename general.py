import requests
import json
import os
import time, datetime

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
    print(obj.convertDateToTimestamp('2018/02/14 16:45:47'))