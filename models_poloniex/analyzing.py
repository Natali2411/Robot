from models_poloniex.authentication import PoloniexAuth

class Analyze(PoloniexAuth):
    obj = PoloniexAuth()
    data = obj.returnTicker()
    bal = obj.returnBalances()

    def strategyTradeViaCoins(self, baseCurrency):
        cur_conf = self.getConfig()["poloniex"][baseCurrency].split(",")
        prices_buy = {}
        prices_sell = {}
        res = {}
        for cur in cur_conf:
            for key, value in self.data.items():
                if baseCurrency + "_" + cur.strip() == key:
                    prices_buy.setdefault(key, value["lowestAsk"])
                    prices_sell.setdefault(key, value["highestBid"])


        return prices_buy


if __name__ == '__main__':
    print(Analyze().strategyTradeViaCoins(baseCurrency="USDT"))

