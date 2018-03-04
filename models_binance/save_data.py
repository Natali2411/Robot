from models_binance.analyzing import Analyzing
from models_binance.gathering_user import GatherUser

class SaveData(Analyzing):
    obj = Analyzing()
    obj2 = GatherUser()

    def saveConvertInfo(self, currency):
        pair = self.obj.getConfig()["conv3Pairs"]
        data = self.obj.convertCurrencyPair()
        balance = self.obj2.getAccountInfo()["balances"]
        for i in balance:
            if i["asset"] == currency:
                s = 'Analyze ' + ' [' + obj.getDateTimeCurrent() + ']: ' + '\n' + \
                'Amount of ' + str(currency) + ' = ' + i["free"] + ', ' + \
                pair["v_symbol1"] + ' (course: ' + data["1"]["v_symbol1"] + '), ' + \
                pair["v_symbol2"] + ' (course: ' + data["2"]["v_symbol2"] + '), ' + \
                pair["v_symbol3"] + ' (course: ' + data["3"]["v_symbol3"] + ');\n'
                res = self.obj.saveDataInFile(data=s)
        return res

if __name__ == '__main__':
    obj = SaveData()
    print(obj.saveConvertInfo("USDT"))