"""
The Main app.
The app starts with getting the strategy and account.
We determine if we are backtesting or running live.
FOR BACKTESTING:
  Do we need to have account run here? Might be able to run account in strategy...
FOR LIVE:
  TODO: Finish fleshing out live.
"""
class SwiftFruit:
  def __init__(self,strategy, account):
    self.strategy = strategy
    self.account = account
    
  def run(self):
    self.strategy.getInfo(self.account)
    if self.account.live:
      self.runLive()
    else:
      self.runTest()

  def runTest(self):
    print("Running test...")
    self.account.update(self.strategy.symbol)
    self.strategy.run()

  def runLive(self):
    pass