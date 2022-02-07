from SwiftFruit import SwiftFruit
from Interval import Interval
from Dates import Dates
from TestAccount import TestAccount
from TestStrategy import TestStrategy

"""
The data on this page is the main data I need to change. 
I need to add in the 'interval', 'dates', the 'strategy', and the 'account'
"""

interval = Interval._1MIN.value
dates = Dates("2020-01-01 00:00:00", "2020-01-01 01:00:00")

print("Making Account...")
account = TestAccount(interval, dates, 100, 0)

print("Making Strategy...")
strategy = TestStrategy()
# TODO: Make account a parameter for strategy. This makes it auto integrated into it

print("Making SwiftFruit...")
swiftFruit = SwiftFruit(strategy, account)
print("Running SwiftFruit...")
swiftFruit.run()