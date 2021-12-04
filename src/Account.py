from binance.client import Client
from numpy import double
from config import API_KEY, API_SECRET
import pprint

class Account:
    def __init__(self):
        self.money = 0
        self.coin = 0
        self.live = False
        self.client = Client(API_KEY, API_SECRET, tld='us')
        trades = self.client.get_historical_klines(symbol='BNBBTC', interval="1m", start_str="2021-21-10")
        #print(trades)

    def update(self):
        pass

    def buy():
        print("Buy!")

    def sell():
        print("Sell!")

    def getHistoricalClosePrices(self, symbol, interval, dates):
        print(interval)
        hist_data = self.client.get_historical_klines(symbol, interval, dates.begin_date, dates.end_date)
        close = []
        for x in hist_data:
            close.append(double(x[4]))
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(close)
        return close