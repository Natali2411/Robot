import requests
import hashlib #!!! API-key format invalid
from models_binance.authentication import Authentication
from general import General
from urllib.parse import urlparse, urlencode


class GatherUser(General, Authentication):
    # Variable for saving base api url
    api = General().getConfig()["gathering"]["base_api"]
    api_key = General().getConfig()["account"]["api_key"]
    api_secret = General().getConfig()["account"]["api_secret"]
    methods = {"getOrderInfo": "/api/v3/order", "getOpenOrders": "/api/v3/openOrders"}

    def getAccountInfo(self):
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).account()
        r = requests.get(url=auth["api_url"], headers=auth["headers"], data=auth["payload"],
                         verify=False)
        return r.json()


    # Check an order's status of user orders. Params: mandatory (symbol, timestamp(LONG)), optional (orderId(LONG),
    # origClientOrderId(STRING), recvWindow(LONG))
    def getOrderInfo(self, v_symbol, v_recvWindow): #, v_orderId='', v_origClientOrderId=''
        #v_symbol = General().encodeParams(v_symbol)
        #v_recvWindow = General().encodeParams(v_recvWindow)
        params = {"symbol": v_symbol, "recvWindow": v_recvWindow}#, "orderId": v_orderId, "origClientOrderId": v_origClientOrderId}
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).orderInfo()
        full_url = auth["api_url"] + '&' + urlencode(params)
        r = requests.request(method=auth['method'], url=full_url, data=auth["payload"], headers=auth["headers"],
                             params=params, verify=False)
        #r = requests.get(url=auth["api_url"], headers=auth["headers"], params=params, data=auth["payload"],
                         #auth=("", ""), verify=False)
        return r.status_code #!!! API-key format invalid

if __name__ == '__main__':
    obj = GatherUser(API_KEY="", API_SECRET="")
    print (obj.getAccountInfo())
