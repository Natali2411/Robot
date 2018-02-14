import pymysql


class RobotDB():
    def __init__(self):
        self.connection = pymysql.connect(self, host='localhost', db='robot', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    def receiveData(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT id, code, name FROM `Currency`"
            cursor.execute(sql)


if __name__ == '__main__':
    obj = RobotDB()
    #print(obj.getTickerInfo('BTCUSD'))
    #print(obj.getStatInfo('BTCUSD'))
    print(obj.receiveData())