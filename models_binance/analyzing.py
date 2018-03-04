from models_binance.gathering_market import Gather
from general import General

class Analyzing(General):
    # Variable for saving base api url
    api = General().getConfig()["gathering"]["base_api"]
    api_key = General().getConfig()["account"]["api_key"]
    api_secret = General().getConfig()["account"]["api_secret"]
    commission = 1 - 0.002 # commission for operation
    gather = Gather()

    # return % of profit or loss
    def convertCurrencyPair(self):
        r1 = {}
        r2 = {}
        r3 = {}
        pair = General().getConfig()["conv3Pairs"]
        #v_symbol1, v_symbol2, v_symbol3
        res = self.gather.getLastPriceTicker()
        for i in range(len(res)):
            if pair["v_symbol1"] == res[i]["symbol"]:
                r1["v_symbol1"] = res[i]["price"]
            if pair["v_symbol2"] == res[i]["symbol"]:
                r2["v_symbol2"] = res[i]["price"]
            if pair["v_symbol3"] == res[i]["symbol"]:
                r3["v_symbol3"] = res[i]["price"]
        oper = round(1 / float(r1["v_symbol1"]) * float(r2["v_symbol2"]) * float(r3["v_symbol3"]) * self.commission,8)
        profit = round(oper * 100 - 100,8)
        r3.update({"profit": profit})
        r = {"1":r1, "2": r2, "3": r3}
        return r

if __name__ == '__main__':
    obj = Analyzing()
    print(obj.convertCurrencyPair())
