import requests
import json
import os


class Gather():
    api = 'https://api.bitfinex.com/'
    # Get a list of symbol names (currencies). Return: list of pairs
    def getCurrencyPairs(self):
        r = requests.get(self.api + 'v1/symbols/')
        return r.json()

    # Get a list with dictionaries of currencies details. Return: pair, price_precision, initial_margin,
    # minimum_margin, maximum_order_size, minimum_order_size, expiration (NA), margin (true, false)
    def getCurrencyDetails(self):
        r = requests.get(self.api + 'v1/symbols_details/')
        return r.json()

    # отримання інформації про найкращу ціну по зазначеній парі валют, обсяги, час:
    # (ціни mid, bid, ask, last_price, low, high; обсяги: volume; час: timestamp)
    def getTickerInfo(self, pair):
        r = requests.get(self.api + 'v1/pubticker/' + pair + '/')
        return r.json()

    # Various statistics about the requested pair (return period, volume)
    def getStatInfo(self, pair):
        r = requests.get(self.api + 'v1/stats/' + pair + '/')
        return r.json()

    # Get the full margin funding book (Інформація про повну фінансову маржу): return rate, amount, period, timestamp, frr
    def getFundBookInfo(self, currency):
        r = requests.get(self.api + 'v1/lendbook/' + currency + '/', verify=False)
        return r.json()

    # Get the full order book. Return: price, amount, timestamp
    def getOrderBookInfo(self, pair):
        r = requests.get(self.api + 'v1/book/' + pair + '/')
        return  r.json()

    # Get a list of the most recent trades for the given symbol. Return: timestamp, tid, price, amount, exchange (bitfinex), type (buy or sell)
    def getTradeInfo(self, pair):
        r = requests.get(self.api + 'v1/trades/' + pair + '/')

    # Get a list of the most recent funding data for the given currency: total amount provided and
    # Flash Return Rate (in % by 365 days) over time. Return: rate, amount_lent, amount_used, timestamp
    def getLendInfo(self, pair):
        r = requests.get(self.api + 'v1/lends/' + pair + '/')

if __name__ == '__main__':
    obj = Gather()
    #print(obj.getTickerInfo('BTCUSD'))
    #print(obj.getStatInfo('BTCUSD'))
    print(obj.getFundBookInfo('USD'))