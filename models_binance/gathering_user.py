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

    # Check an order's status of user orders. Params: mandatory (symbol, timestamp(LONG)), optional (orderId(LONG),
    # origClientOrderId(STRING), recvWindow(LONG))
    def getOrderInfo(self, v_symbol, v_datetime, v_orderId=None, v_origClientOrderId=None, v_recvWindow=None):
        v_timestamp = General().convertDateToTimestamp(v_datetime)
        params = {"symbol": v_symbol, "timestamp": v_timestamp, "orderId": v_orderId,
                  "origClientOrderId": v_origClientOrderId, "recvWindow": v_recvWindow}
        r = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret, params=params).orderInfo()

        return r #!!! API-key format invalid


    # Get all open orders on a symbol. Careful when accessing this with no symbol. Params: mandatory(timestamp), optional(symbol, recvWindow(LONG))
    def getOpenOrders(self, v_datetime, v_symbol=None, v_recvWindow=None):

        v_timestamp = General().convertDateToTimestamp(v_datetime)
        r = requests.get(General().makeAuthApi(api_key=self.api_key, api_secret=self.api_secret, method_url=self.methods["getOpenOrders"]),
                         params={"symbol": v_symbol, "recvWindow": v_recvWindow, "timestamp": v_timestamp}, verify=False)
        return r.json() #!!! API-key format invalid


if __name__ == '__main__':
    obj = GatherUser(API_KEY="",
                     API_SECRET="")
    print(obj.getOrderInfo(v_symbol='BTCUSDT', v_datetime='2018/02/14 16:45:47'))