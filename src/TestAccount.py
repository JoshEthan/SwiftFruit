from Account import Account
import pprint
from Interval import Interval
from datetime import datetime


"""
TestAccount:
    __init__:   When the account starts it will start with set amount of coins and money.
                In addition, the 'self.live' will determine if the account will use live data or historical.

    update:     This function is called every iteration. This one should update the price information.
                This will include the historical price list or live price data.
    
    buy:        Use the API to perform an actual purchase.

    sell:       Use the API to perform an actual sell.

"""
class TestAccount(Account):
    def __init__(self, interval, dates, money, coin):
        super().__init__(interval, dates)
        self.money = money
        self.coin = coin
        self.live = False
        print("Test Account - init: \n\t Money: {} \n\t Coin: {}".format(money, coin))

    def update(self, symbol):
        self.symbol = symbol
        self.now = datetime.now()
        print(self.now)
        print("CREATING SHEET...")
        self.row[0] = self.now.strftime("%H:%M:%S\n%m/%d/%Y")
        self.row[1] = self.live
        self.row[2] = self.money
        self.row[3] = self.coin

        self.sheets.add_row(self.row)
        # trades = self.client.get_historical_klines(symbol='BNBBTC', interval="1m", start_str="2021-21-10")
        # self.client.get_server_time() -> Get current time
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.client.get_orderbook_tickers())
        self.historical_close_prices = self.getHistoricalClosePrices(self.symbol, self.interval, self.dates)
        pass

    def buy(self, price):
        self.coin = self.money / price
        self.money = 0
        print("Test Strategy - Buy: \n\t Account Money: {} \n\t Price: {} \n\t Account Coin: {}".format(self.money, price, self.coin))


    def sell(self, price):
        self.money = self.coin * price
        self.coin = 0
        print("Test Strategy - Sell: \n\t Account Money: {} \n\t Price: {} \n\t Account Coin: {}".format(self.money, price, self.coin))