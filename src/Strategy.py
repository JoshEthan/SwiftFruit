from binance.client import Client
from config import API_KEY, API_SECRET

class Strategy:
    def __init__(self):
        self.money = 0

    def getInfo(self, interval, dates, account):
        pass

    def run(self):
        pass

    def buy(self):
        print("Buy!")

    def sell(self):
        print("Sell!")