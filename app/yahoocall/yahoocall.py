import yfinance as yf
import locale

test_portfolio = ["MSFT"]

locale.setlocale(locale.LC_ALL, '')

class YahooCall:
    
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def getData(self):
        for stock in self.portfolio:
            stockdata = yf.Ticker(stock).info
            ebitda = stockdata['ebitda']
            return f"{ebitda:,d}", stockdata['financialCurrency']

caller = YahooCall(test_portfolio)
print(caller.getData())