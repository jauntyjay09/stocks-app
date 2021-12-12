import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

first_level=0
second_level=0
third_level=0
fourth_level=0
max_price=0
min_price=0



def fibanocii(data):  
  df=data
  max_price=df['close'].max()
  min_price=df['close'].min()
  diff=max_price-min_price

  first_level=max_price - diff* 0.236
  second_level=max_price - diff* 0.382
  third_level=max_price - diff* 0.5
  fourth_level=max_price - diff* 0.618

  #calculating MACd line and signal  line
  shortema = df.close.ewm(span=12,adjust=False).mean()
  longema=df.close.ewm(span=26,adjust=False).mean()

  macd= shortema-longema

  signal = macd.ewm(span=9,adjust=False).mean()

  df['macd']=macd
  df['signal']=signal
  df.head()
  buy,sell=strategy(df)
  df['buy_signal_price']=buy
  df['sell_signal_price']=sell

  new_df = df
  #plot fibonacci level 

  plt.figure(figsize=(12,9))
  plt.plot(new_df.index,new_df['close'],alpha=0.5)
  plt.scatter(new_df.index,new_df['buy_signal_price'],color='green',marker='^',alpha=1)
  plt.scatter(new_df.index,new_df['sell_signal_price'],color='red',marker='^',alpha=1)
  plt.axhline(max_price,linestyle='--',alpha=0.5,color='red')
  plt.axhline(first_level,linestyle='--',alpha=0.5,color='orange')
  plt.axhline(second_level,linestyle='--',alpha=0.5,color='yellow')
  plt.axhline(third_level,linestyle='--',alpha=0.5,color='green')
  plt.axhline(fourth_level,linestyle='--',alpha=0.5,color='blue')
  plt.axhline(min_price,linestyle='--',alpha=0.5,color='purple')
  plt.ylabel('close price')
  plt.xlabel('Date')
  plt.xticks(rotation=45)
  plt.show()

def getlevels(price):
    if price>=first_level:
      return(max_price,first_level)
    elif price>=second_level:
      return(first_level,second_level)
    elif price>=third_level:
      return(second_level,third_level)
    elif price>=fourth_level:
      return(third_level,fourth_level)
    else:
      return(fourth_level,min_price)

#if the signal line crosses above the macd line and the current price crossed above or below the last fibonacci level then buy
#if the signal line crosses below the macd line and the current price crossed above or below the last fibonacci level then sell

def strategy(df):
  buylist=[]
  selllist=[]
  flag=0
  last_buy_price=0

  for i in range(0,df.shape[0]):
    price = df['close'][i]
    #FIRST DATA POINT
    if i==0:
      upper_level,lower_level=getlevels(price)
      buylist.append(np.nan)
      selllist.append(np.nan)
  
    elif price>=upper_level or price<=lower_level:
      #check to see if the macd crossed above or below the signal line
      if df['signal'][i]>df['macd'][i] and flag==0:
        last_buy_price = price
        buylist.append(price)
        selllist.append(np.nan)
        flag=1
      elif df['signal'][i]<df['macd'][i] and flag==1 and price>last_buy_price:
        buylist.append(np.nan)
        selllist.append(price)
        flag=0
      else:
        buylist.append(np.nan)
        selllist.append(np.nan)
    else:
      buylist.append(np.nan)
      selllist.append(np.nan)

  #update levels
    upper_level,lower_level=getlevels(price)
  return buylist,selllist

