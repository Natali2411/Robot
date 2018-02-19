import requests
import hashlib #!!! API-key format invalid
from models_binance.authentication import Authentication
from general import General


class Trading(General, Authentication):
    # Variable for saving base api url
    api = General().getConfig()["gathering"]["base_api"]
    api_key = General().getConfig()["account"]["api_key"]
    api_secret = General().getConfig()["account"]["api_secret"]

    # Send in a new order. Params: mandatory(symbol, side, type, quantity, timestamp in payload), optional(timeInForce, price,
    # newClientOrderId, stopPrice, icebergQty, newOrderRespType)
    def postNewOrder(self, v_symbol, v_side, v_type, v_quantity, v_timeInForce=None, v_price=None, v_newClientOrderId=None,
                     v_stopPrice=None, v_icebergQty=None, v_newOrderRespType=None):
        params = {"symbol": v_symbol, "side": v_side, "type": v_type, "quantity": v_quantity, "timeInForce": v_timeInForce,
                  "price": v_price, "newClientOrderId": v_newClientOrderId, "stopPrice": v_stopPrice, "icebergQty": v_icebergQty,
                  "newOrderRespType": v_newOrderRespType}
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).createOrder()
        r = requests.post(url=auth["api_url"], headers=auth["headers"], data=auth["payload"], params=params, verify=False)
        return r.json()

    # Cancel an active order. Params: mandatory(symbol, timestamp in payload), optional(orderId, origClientOrderId, newClientOrderId, recvWindow)
    def delCancelOrder(self, v_symbol, v_orderId=None, v_origClientOrderId=None, v_newClientOrderId=None, v_recvWindow=None):
        params = {"symbol": v_symbol, "orderId": v_orderId, "origClientOrderId": v_origClientOrderId,
                  "newClientOrderId": v_newClientOrderId, "recvWindow": v_recvWindow}
        auth = Authentication(API_KEY=self.api_key, API_SECRET=self.api_secret).cancelOrder()
        r = requests.delete(url=auth["api_url"], headers=auth["headers"], data=auth["payload"], params=params, verify=False)
        return r.json()


if __name__ == '__main__':
    obj = Trading(API_KEY="", API_SECRET="")
    obj.postNewOrder(v_symbol="LTCETH")
