import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web

tickers = ['AAPL','TSLA','FB','AMZN','NVDA']
amounts = [7,5,12,16,2,4]
prices = []
total = []

# someboolean = True
# while(someboolean):
#     tickers = input("What stock do you want to add ?")
#     amount = input("What is the amount")

for ticker in tickers:
    df = web.DataReader(ticker,'yahoo',dt.datetime(2019,8,1),dt.datetime.now())
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = prices.index(price)
    total.append(price * amounts[index])

# print(prices)
# print(total)

fig, ax = plt.subplots(figsize=(16,8))

ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')

ax.tick_params(axis='x',color='white')
ax.tick_params(axis='y',color='white')

ax.set_title('PRATIKs STOCKS VISUALIZER',color='#EF6C35',fontname='Times New Roman',fontsize=20)
_, texts, _ = ax.pie(total,labels=tickers, autopct="%1.1f%%", pctdistance=0.8)
[text.set_color('white') for text in texts]

my_circle=plt.Circle((0,0),0.55,color='black')
plt.gca().add_artist(my_circle)

ax.text(-2,1,'PORTFOLIO OVERVIEW',fontname='Times New Roman',color='#FFE536',verticalalignment='center',horizontalalignment='center')
ax.text(-2,0.85,f'Total USD Amount : {sum(total):2f} $',fontsize=12,color='white',verticalalignment='center',horizontalalignment='center')

counter = 0.15
for ticker in tickers:
    ax.text(-2,0.85 - counter, f'{ticker}:{total[tickers.index(ticker)]:.2f}$', fontsize= 12,color = 'white',verticalalignment='center',horizontalalignment='center')
    counter += 0.15

plt.show()