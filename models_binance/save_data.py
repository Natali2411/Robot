from models_binance.analyzing import Analyzing


class SaveData(Analyzing):
    obj = Analyzing()

    def saveConvertInfo(self):
        data = self.obj.convertCurrencyPair()
        data.update("")
        self.obj.saveDataInFile(data=data)
        return 'Yes'

if __name__ == '__main__':
    obj = SaveData()
    print(obj.saveConvertInfo())