import datetime as dt                            #Importing the date time
import pandas_datareader as web                  # For reading the data
import matplotlib.pyplot as plt                  # For graph plotting
import matplotlib.dates as mdates                # Plotting the dates
from mpl_finance import candlestick_ohlc         # For fetching the candlestick pattern

#Starting date and ending date
ticker = 'AAPL'
start = dt.datetime(2019,1,1)
end = dt.datetime.now()

#Loading the dataset
#ticker ='Share'
ticker = 'AAPL'
data = web.DataReader(ticker,'yahoo',start,end)
print(data)
print(data.columns)

#Restructure the Data
data = data[['Open','High','Low','Close']]

#Resetting the index
data.reset_index(inplace=True)
data['Date'] =data['Date'].map(mdates.date2num)
print(data)

#Plotting the data
#Visualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('{}Share Price'.format(ticker),color = 'white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis = 'x', color = 'white')
ax.tick_params(axis = 'y', color = 'white')
ax.xaxis_date()
candlestick_ohlc(ax,data.values,width=0.5,colorup='#00ff00')
plt.show()