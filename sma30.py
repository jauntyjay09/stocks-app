
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sma30(data):
  
  data['SMA30']=data['close'].rolling(window=30).mean()
  buy=[]
  sell=[]
  flag=0
  buy_price=0
  for i in range(0,len(data)):
    if data['SMA30'][i]>data['close'][i] and flag==0:
      buy.append(data['close'][i])
      sell.append(np.nan)
      buy_price=data['close'][i]
      flag=1
    elif data['SMA30'][i]<data['close'][i] and flag==1 and buy_price<data['close'][i]:
      sell.append(data['close'][i])
      buy.append(np.nan)
      flag=0
      buy_price=0
    else: 
      sell.append(np.nan)
      buy.append(np.nan)
  data['Buy'],data['Sell']=buy,sell


  #printing the graph here
  plt.figure(figsize=(12,6))
  plt.title('BUy and Sell signals using SMA 30')
  plt.plot(data['close'],alpha=0.5)
  plt.plot(data['SMA30'],alpha=0.5)
  plt.scatter(data.index,data['Buy'],color='green',marker='*',alpha=1)
  plt.scatter(data.index,data['Sell'],color='red',marker='*',alpha=1)
  plt.title('Price')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.xticks(rotation=45)
  plt.show()
  

