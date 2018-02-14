import requests
import json
import os

class General():
    api = "https://api.binance.com/"

    def getConfig(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "config.json"))
        with open(filename)as f:
            return json.load(f)
        #return print(filename)


if __name__ == '__main__':
    obj = General()
    print(obj.getConfig())