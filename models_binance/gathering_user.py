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
        return auth["api_url"]


    # Check an order's status of user orders. Params: mandatory (symbol, timestamp(LONG)), optional (orderId(LONG),
    # origClientOrderId(STRING), recvWindow(LONG))
    def getOrderInfo(self, v_symbol, v_recvWindow): #, v_orderId='', v_origClientOrderId=''
        params = {"symbol": v_symbol, "recvWindow": v_recvWindow}#, "orderId": v_orderId, "origClientOrderId": v_origClientOrderId}
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).orderInfo()
        full_url = auth["api_url"] + '&' + urlencode(params)
        r = requests.request(method=auth['method'], url=full_url, headers=auth["headers"], verify=False)
        return full_url #!!! API-key format invalid

    def getOpenOrders(self): #, v_orderId='', v_origClientOrderId=''
        #params = {"symbol": v_symbol, "recvWindow": v_recvWindow}#, "orderId": v_orderId, "origClientOrderId": v_origClientOrderId}
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).openOrders()
        #full_url = auth["api_url"] + '&' + urlencode(params)
        r = requests.request(method=auth['method'], url=auth["api_url"], headers=auth["headers"], data=auth["payload"], verify=False)
        return r.json() #!!! API-key format invalid

    def getAllOrders(self, v_symbol, v_recvWindow):
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).allOrders()
        params = {"symbol": v_symbol, "recvWindow": v_recvWindow}#, "orderId": v_orderId, "origClientOrderId": v_origClientOrderId}
        r = requests.request(method=auth['method'], url=auth["api_url"], headers=auth["headers"],
                             params=urlencode(params), verify=False)
        return r.text #!!! API-key format invalid


if __name__ == '__main__':
    obj = GatherUser(API_KEY="",
                     API_SECRET="")
    #print (obj.getAccountInfo())
    #print (obj.getOrderInfo(v_symbol="LTCETH", v_recvWindow=60000000))
    #print (obj.getOpenOrders())
    print (obj.getAllOrders(v_symbol="LTCETH", v_recvWindow=60000000))