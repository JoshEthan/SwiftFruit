from Strategy import Strategy
import numpy, talib

class TestStrategy(Strategy):
    def __init__(self):

        self.symbol = "DOGEUSDT"

    def getInfo(self, interval, dates, account):
        self.account = account
        self.interval = interval
        self.dates = dates
        pass

    def run(self):
        close1 = self.account.getHistoricalClosePrices(self.symbol, self.interval, self.dates)
        close1 = numpy.array(close1)
        output = talib.RSI(close1)
        for x in output:
            shouldBuy = x < 30 and self.account.money > 0
            shouldSell = x > 70  and self.account.coin > 0
            if shouldBuy:
                self.buy(x)
            elif shouldSell:
                self.sell(x)
            else:
                pass
                #print("No action.")

    def buy(self, price):
        self.account.coin = self.account.money * price
        print(self.account.money)
        print(price)
        print("Buy!: {}".format(self.account.coin))
        self.account.money = 0

    def sell(self, price):
        self.account.money = self.account.coin * price
        print("Sell!: {}".format(self.account.money))
        self.account.coin = 0