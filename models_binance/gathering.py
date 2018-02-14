import requests
from models_binance.general import General

class Gather(General):
    #t= self.getConfig()["gathering"]["base_api"]
    def getPriceTicker(self):
        r = requests.get(self.api + '/api/v3/ticker/price', verify=False)
        return r.json()




if __name__ == '__main__':
    obj = Gather()
    #print(obj.getTickerInfo('BTCUSD'))
    #print(obj.getStatInfo('BTCUSD'))
    print(obj.getPriceTicker())