#Module1 - Importing the libraries

import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

#Module2 - Defining the crypto

crypto = 'BTC'
currency = "USD"

#Defining the start and end time
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

btc = web.DataReader(f"{crypto}-{currency}","yahoo",start,end)
eth = web.DataReader(f"ETH-{currency}","yahoo",start,end)

plt.plot(btc['Close'], label="BTC")
plt.plot(eth['Close'], label="ETH")
plt.legend(loc = "upper left")
plt.show()
