import requests
import json
import os

class General():
    api = "https://api.binance.com/"

    def getConfig(self):
        path = os.path.abspath(os.path.dirname(__file__))
        filename = os.path.join(os.path.split(path)[0], 'config.json')
        with open(filename)as f:
            return json.load(f)
        #return print(filename)


if __name__ == '__main__':
    obj = General()
    print(obj.getConfig())