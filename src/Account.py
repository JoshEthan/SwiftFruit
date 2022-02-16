from binance.client import Client
from numpy import double
from Interval import Interval
from config import API_KEY, API_SECRET
from GoogleSheets import Sheets
import pprint
from datetime import datetime

class Account:
    def __init__(self, interval, dates):
        self.interval = interval
        self.dates = dates
        self.symbol = ""
        self.money = 0
        self.coin = 0
        self.live = False
        self.historical_close_prices = None
        self.now = datetime.now()
        self.sheets = Sheets()
        self.row = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        print("Get Client:", self.now.strftime("%H:%M:%S"))
        self.client = Client(API_KEY, API_SECRET, tld='us')
        trades = self.client.get_historical_klines(symbol='BNBBTC', interval="1m", start_str="2021-21-10")
        #print(trades)

    def update(self):
        self.now = datetime.now()
        self.row[0] = self.now
        self.sheets.add_row(self.row)
        print("Update:", self.now.strftime("%H:%M:%S"))
        

    def buy():
        print("Buy!")

    def sell():
        print("Sell!")

    def getHistoricalClosePrices(self, symbol, interval, dates):
        print("Getting historic data...")
        hist_data = self.client.get_historical_klines(symbol, interval, dates.begin_date, dates.end_date)
        close = []
        for x in hist_data:
            close.append(double(x[4]))
        pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(close)
        return close