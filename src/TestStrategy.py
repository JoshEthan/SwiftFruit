from Strategy import Strategy
import numpy, talib
import time
"""
TestStrategy:
    __init__:   When the strategy starts this should start values that should be known.

    getInfo:    Instantiate the needed info for the strategy.
                    account     - The users account object
                    interval    - The time interval (1m, 5m, etc)
                    dates       - The time frame
    
    run:        This method is called when we want to run the strategy.

    buy:        What should happen when we want to sell.

    sell:       What should happen when we want to buy.

"""
class TestStrategy(Strategy):
    def __init__(self):
        self.symbol = "DOGEUSDT"

    def getInfo(self, account):
        self.account = account
        self.interval = account.interval
        self.dates = account.dates

    def run(self):
        #historical_close_prices = self.account.getHistoricalClosePrices(self.symbol, self.interval, self.dates)
        historical_close_prices = numpy.array(self.account.historical_close_prices)
        rsi_values = talib.RSI(historical_close_prices)
        #print("Test Strategy - Run: \n\t historical_close_prices: {}".format(historical_close_prices))
        for i, price in enumerate(historical_close_prices):
            self.account.row[4] = price
            print(rsi_values[i])
            if rsi_values[i] != None:
                self.account.row[5] = "-"
            else:
                self.account.row[5] = rsi_values[i]
            print(self.account.row[5])
            #self.account.row[5] = rsi_values[i]
            shouldBuy = rsi_values[i] < 30 and self.account.money > 0
            shouldSell = rsi_values[i] > 70  and self.account.coin > 0
            #print("Test Strategy - Run: \n\t RSI: {} \n\t Price: {}".format(rsi_values[i], price))
            if shouldBuy:
                self.buy(price)
            elif shouldSell:
                self.sell(price)
            else:
                pass
                #print("Test Strategy - Action: No buy. No sell.")
            self.account.sheets.add_row(self.account.row)
            time.sleep(2)

    def buy(self, price):
        self.account.buy(price)
        
    def sell(self, price):
        self.account.sell(price)
        