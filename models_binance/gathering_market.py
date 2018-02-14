import requests
from general import General


class Gather(General):
    # Variable for saving base api
    api = General().getConfig()["gathering"]["base_api"]
    # Test connectivity to the Rest API and get the current server time. Return: serverTime
    def getServerTime(self):
        r = requests.get(self.api + '/api/v1/time', verify=False)
        return r.json()

    # Current exchange trading rules and symbol information. Return: see documentation.
    def getExchangeInfo(self):
        r = requests.get(self.api + '/api/v1/exchangeInfo', verify=False)
        return r.json()

    # Current order book. Params: limit (Default 100; max 1000. Valid limits:[5, 10, 20, 50, 100, 500, 1000]), symbol(pair)
    def getOrderBook(self, v_symbol, v_limit=100):
        r = requests.get(self.api + '/api/v1/depth', params={"symbol": v_symbol, "limit": v_limit}, verify=False)
        return r.json()

    # Get recent trades (up to last 500). Params: limit (Default 500; max 500), symbol(pair)
    def getTradeList(self, v_symbol, v_limit=500):
        r = requests.get(self.api + '/api/v1/trades', params={"symbol": v_symbol, "limit": v_limit}, verify=False)
        return r.json()

    # Get old trades on the market. Params: limit (Default 500; max 500), symbol(pair), fromId (TradeId to fetch from. Default gets most recent trades.)
    def getOldTrades(self, v_symbol, v_limit=500, v_fromId=None):
        r = requests.get(self.api + '/api/v1/historicalTrades', params={"symbol": v_symbol, "limit": v_limit, "fromId": v_fromId}, verify=False)
        return r.json()

    # Get compressed, aggregate trades. Trades that fill at the time, from the same order, with the same price will have the quantity aggregated.
    # Params: mandatory (symbol), optional (fromId=ID to get aggregate trades from INCLUSIVE; startTime,
    # endTime=Timestamp in ms to get aggregate trades from/to INCLUSIVE; limit (Default 500; max 500))
    def getAggregateList(self, v_symbol, v_fromId=None, v_startTime=None, v_endTime=None, v_limit=500):
        r = requests.get(self.api + '/api/v1/historicalTrades', params={"symbol": v_symbol, "fromId": v_fromId, "startTime": v_startTime,
                                                                        "endTime": v_endTime, "limit": v_limit}, verify=False)
        return r.json()

    # Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
    # Params: mandatory (symbol, interval), optional (startTime, endTime, limit (Default 500; max 500))
    def getCandlestickInfo(self, v_symbol, v_interval, v_startTime=None, v_endTime=None, v_limit=500):
        r = requests.get(self.api + '/api/v1/klines', params={"symbol": v_symbol, "interval": v_interval, "startTime": v_startTime,
                                                              "endTime": v_endTime, "limit": v_limit}, verify=False)
        return r.json()

    # 24 hour price change statistics. Careful when accessing this with no symbol. Params: optional (symbol)
    def getPriceTicker(self, v_symbol=None):
        r = requests.get(self.api + '/api/v1/ticker/24hr', params={"symbol": v_symbol}, verify=False)
        return r.json()

    # Latest price for a symbol or symbols. Params: optional (symbol)
    def getLastPriceTicker(self, v_symbol=None):
        r = requests.get(self.api + '/api/v3/ticker/price', params={"symbol": v_symbol}, verify=False)
        return r.json()

    # Best price/qty on the order book for a symbol or symbols. Params: optional (symbol)
    def getBestPrice(self, v_symbol=None):
        r = requests.get(self.api + '/api/v3/ticker/bookTicker', params={"symbol": v_symbol}, verify=False)
        return r.json()

if __name__ == '__main__':
    obj = Gather()
    print(obj.getBestPrice(v_symbol='BTCUSDT'))