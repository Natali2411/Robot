from models_binance.gathering_market import Gather
from general import General

class Analyzing(General):
    # Variable for saving base api url
    api = General().getConfig()["gathering"]["base_api"]
    api_key = General().getConfig()["account"]["api_key"]
    api_secret = General().getConfig()["account"]["api_secret"]
    gather = Gather()

    def convertCurrencyPair(self, v_symbol1, v_symbol2, v_symbol3, v_symbol4):
        r = {}
        res = self.gather.getPriceTicker()
        for i in range(len(res)):
            if v_symbol1 == res[i]["symbol"]:
                r[v_symbol1] = res[i]["askPrice"]
            if v_symbol2 == res[i]["symbol"]:
                r[v_symbol2] = res[i]["askPrice"]
            if v_symbol3 == res[i]["symbol"]:
                r[v_symbol3] = res[i]["askPrice"]
            if v_symbol4 == res[i]["symbol"]:
                r[v_symbol4] = res[i]["askPrice"]
        if len(r) == 2:
            rate = float(r[v_symbol2])/float(r[v_symbol1])*float(r[v_symbol3])*float(r[v_symbol4])
        return rate

if __name__ == '__main__':
    obj = Analyzing()
    print(obj.convertCurrencyPair('ETHBTC', 'ETHUSDT', 'ETHLTC', 'ETHAMB'))
