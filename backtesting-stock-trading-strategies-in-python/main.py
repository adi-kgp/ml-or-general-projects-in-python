from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA, GOOG
import talib
import yfinance as yf
import datetime as dt

# class MySMAStrategy(Strategy):

#     def init(self):
#         price = self.data.Close
#         self.ma1 = self.I(SMA, price, 10)
#         self.ma2 = self.I(SMA, price, 20)
    
#     def next(self):
#         if crossover(self.ma1, self.ma2):
#             self.buy()
#         elif crossover(self.ma2, self.ma1):
#             self.sell()

# backtest = Backtest(GOOG, MySMAStrategy, commission=.002, exclusive_orders=True)
# stats = backtest.run()

# print(stats)

# backtest.plot()

class MyMACDStrategy(Strategy):

    def init(self):
        price = self.data.Close
        self.macd = self.I(lambda x: talib.MACD(x)[0], price)
        self.macd_signal = self.I(lambda x: talib.MACD(x)[1], price)

    def next(self):
        if crossover(self.macd, self.macd_signal):
            self.buy()
        elif crossover(self.macd_signal, self.macd):
            self.sell()


start = dt.datetime(2020, 1, 1)
end = dt.datetime(2022, 1, 1)

data = yf.download("TSLA", start, end)

backtest = Backtest(data, MyMACDStrategy, commission=0.002, exclusive_orders=True)

print(backtest.run())

backtest.plot()