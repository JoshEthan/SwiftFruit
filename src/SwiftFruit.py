from Account import Account

class SwiftFruit:
  def __init__(self, interval, dates, strategy, account):
    self.interval = interval
    self.dates = dates
    self.strategy = strategy
    self.account = account

  def run(self):
    self.strategy.getInfo(self.interval, self.dates, self.account)
    if self.account.live:
      self.runLive()
    else:
      self.runTest()

  def runTest(self):
    self.account.update()
    self.strategy.run()

  def runLive(self):
    pass