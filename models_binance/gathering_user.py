import requests
import hashlib #!!! API-key format invalid
from models_binance.authentication import Authentication
from general import General


class GatherUser(General, Authentication):
    # Variable for saving base api url
    api = General().getConfig()["gathering"]["base_api"]
    api_key = General().getConfig()["account"]["api_key"]
    api_secret = General().getConfig()["account"]["api_secret"]
    methods = {"getOrderInfo": "/api/v3/order", "getOpenOrders": "/api/v3/openOrders"}

    def getAccountInfo(self):
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).account()
        r = requests.get(url=auth["api_url"], headers=auth["headers"], data=auth["payload"], verify=False)
        return r.json()


    # Check an order's status of user orders. Params: mandatory (symbol, timestamp(LONG)), optional (orderId(LONG),
    # origClientOrderId(STRING), recvWindow(LONG))
    def getOrderInfo(self, v_symbol, v_recvWindow, v_orderId=None, v_origClientOrderId=None):
        #v_timestamp = General().convertDateToTimestamp(v_datetime)
        params = {"symbol": v_symbol, "orderId": v_orderId, "origClientOrderId": v_origClientOrderId, "recvWindow": v_recvWindow}
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).orderInfo()
        auth["payload"].update(params)
        #r = requests.request(method=auth['method'], url=auth["api_url"], data=auth["payload"], headers=auth["headers"], params=params, verify=False)
        r = requests.get(url=auth["api_url"], headers=auth["headers"], params=auth["payload"], verify=False)
        return auth["api_url"]#!!! API-key format invalid


if __name__ == '__main__':
    obj = GatherUser(API_KEY="",
                     API_SECRET="")
    print(obj.getOrderInfo(v_symbol='ETHLTC', v_recvWindow=600000))

          #(v_symbol='ETHLTC', v_recvWindow=600000))