import requests
from general import General


class GatherUser(General):
    # Variable for saving base api url
    api = General().getConfig()["gathering"]["base_api"]

    # Check an order's status of user orders. Params: mandatory (symbol, timestamp(LONG)), optional (orderId(LONG),
    # origClientOrderId(STRING), recvWindow(LONG))
    def getOrderInfo(self, v_symbol, v_timestamp, v_orderId=None, v_origClientOrderId=None, v_recvWindow=None):
        r = requests.get(self.api + '/api/v3/order', params={"symbol": v_symbol, "timestamp": v_timestamp, "orderId": v_orderId,
                                                             "origClientOrderId": v_origClientOrderId, "recvWindow": v_recvWindow}, verify=False)
        return r.json()





if __name__ == '__main__':
    obj = GatherUser()
    print(obj.getOrderInfo(v_symbol='BTCUSDT', v_timestamp))