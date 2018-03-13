from models_binance.analyzing import Analyzing
from models_binance.gathering_user import GatherUser
from models_binance.gathering_market import Gather
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
import time
from apscheduler.schedulers.blocking import BlockingScheduler

class SaveData(Analyzing):
    obj = Analyzing()
    obj2 = GatherUser()
    obj3 = Gather()

    def saveConvertInfo(self, currency):
        res = ''
        pair = self.obj.getConfig()["conv3Pairs"]
        data = self.obj.convertCurrencyPair()
        balance = self.obj2.getAccountInfo()["balances"]
        for i in balance:
            if i["asset"] == currency:
                s = 'Analyze ' + ' [' + obj.getDateTimeCurrent() + ']: ' + '\n' + \
                'Amount of ' + str(currency) + ' = ' + i["free"] + ', ' + \
                pair["v_symbol1"] + ' (course: ' + data["1"]["v_symbol1"] + '), ' + \
                pair["v_symbol2"] + ' (course: ' + data["2"]["v_symbol2"] + '), ' + \
                pair["v_symbol3"] + ' (course: ' + data["3"]["v_symbol3"] + '), profit: ' + str(data["3"]["profit"]) + ';\n'
                res = self.obj.saveDataInFile(data=s)
        return res

    def createSchedSaveData(self):
        sched = BlockingScheduler()
        @sched.scheduled_job('interval', minutes=1)
        def startSched(self):
            self.saveConvertInfo(currency=self.obj.getConfig()["convCurrSave"])
        self.sched.start()

        #@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)


if __name__ == '__main__':
    obj = SaveData()
    #print(obj.saveConvertInfo("USDT"))
    print(obj.createSchedSaveData())


'''from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()'''