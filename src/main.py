from SwiftFruit import SwiftFruit
from Interval import Interval
from Dates import Dates
from TestAccount import TestAccount
from TestStrategy import TestStrategy

interval = Interval._1MIN.value
dates = Dates("2020-01-01 00:00:00", "2020-01-01 11:59:59")

strategy = TestStrategy()
# account = TestAccount(100, 0)

# swiftFruit = SwiftFruit('1m', dates, strategy, account)
# swiftFruit.run()