from SwiftFruit import SwiftFruit
from Interval import Interval
from Dates import Dates
from TestAccount import TestAccount
from TestStrategy import TestStrategy
import logging
from SF_LOG import SF_LOGGER

LOG = SF_LOGGER('main', 1)

LOG.INFO("Starting.")

# logging.basicConfig(filename='myapp.log', format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG)
# logging.info('Starting Swift Fruit.')


interval = Interval._1MIN.value
dates = Dates("2020-01-01 00:00:00", "2020-01-01 11:59:59")
LOG.DEBUG('Interval', interval)
LOG.DEBUG('Dates', dates)
strategy = TestStrategy()
# account = TestAccount(100, 0)
# logging.debug('Interval: ', interval)
# logging.debug('Dates: ', dates)

# logging.debug('Interval: ', interval)
# swiftFruit = SwiftFruit('1m', dates, strategy, account)
# swiftFruit.run()

# logging.info('Closing Swift Fruit.')