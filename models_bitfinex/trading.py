import requests
from models_bitfinex.gathering import Gather


class Trading(Gather):
    # create new order: side = buy or sell, type = market, limit, stop, trailing-stop and etc.
    def createNewOrder(self, currency, sumOrder, priceOrder, tradeOper, typeOper):
        r = requests.post(self.api + 'v1/order/new/', data={"symbol": currency, "amount": sumOrder, "price": priceOrder,
                                                            "side": tradeOper, "type": typeOper, "exchange": "bitfinex",
                                                            "buy_price_oco": "0", "sell_price_oco": "0"})
        #insert order_id n db
        return r.json()

    # cancel order by id

    def cancelOrder(self, orderId):
        r = requests.post(self.api + "v1/order/cancel/", data={"order_id": orderId})
        return r.status_code

    # Get the status of an order. Is it active? Was it cancelled? To what extent has it been executed? etc.
    def checkOrderStatus(self, orderId):
        r = requests.post(self.api + "v1/order/status/", data={"order_id": orderId})
        return r.json()