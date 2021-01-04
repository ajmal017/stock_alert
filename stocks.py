from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='F3DMO3H539P6UIJE', output_format='pandas')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('IBM')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()


import quandl
data3 = quandl.get("WIKI/KO", start_date="2016-01-01", end_date="2018-01-01", api_key='osKzd8fbLqC4xDKzcEfK')
data3.Close.plot()
plt.show()


import yfinance as yf

# Get the data of the stock AAPL
data = yf.download('AAPL', '2016-01-01', '2018-01-01')

# Plot the close price of the AAPL
data.Close.plot()
plt.show()

import urllib2
import json
import time

import urllib2
import json
import time


class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="

    def get(self, symbol, exchange):
        url = self.prefix + "%s:%s" % (exchange, symbol)
        u = urllib2.urlopen(url)
        content = u.read()

        obj = json.loads(content[3:])
        return obj[0]


if __name__ == "__main__":
    c = GoogleFinanceAPI()

    while 1:
        quote = c.get("MSFT", "NASDAQ")
        print (quote)
        time.sleep(30)