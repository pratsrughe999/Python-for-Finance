import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt

ticker = 'FB'
start = dt.datetime(2019,1,1)
end = dt.datetime.now()

df = web.DataReader(ticker,'yahoo',start,end)
print(df.head(5))