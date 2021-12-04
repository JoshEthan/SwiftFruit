from Account import Account
import pprint

from Interval import Interval

class TestAccount(Account):
    def __init__(self, money, coin):
        super().__init__()
        self.money = money
        self.coin = coin
        self.live = False

    def update(self):
        trades = self.client.get_historical_klines(symbol='BNBBTC', interval="1m", start_str="2021-21-10")
        # self.client.get_server_time() -> Get current time
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(self.client.get_orderbook_tickers())
        pass

    def buy():
        print("Buy!")

    def sell():
        print("Sell!")