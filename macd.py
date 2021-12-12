
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def macd_(data):
  df=data
  df['20day']=df['close'].rolling(window=20).mean()
  df['50day']=df['close'].rolling(window=50).mean()


  df['signal']=np.where(df['20day']>df['50day'],1,0)
  df['position']=df['signal'].diff()

  df['buy']=np.where(df['position']==1,df['close'],np.NaN)
  df['sell']=np.where(df['position']==-1,df['close'],np.NaN)

  plt.figure(figsize=(16,8))
  plt.title('close price history....buy and sell signals',fontsize = 18)
  plt.plot(df.close,alpha=0.5,label='close')
  plt.plot(df['20day'],alpha=0.5,label='SMA20')
  plt.plot(df['50day'],alpha=0.5,label='SMA50')
  plt.scatter(df.index,df['buy'],alpha=1,label='buysignal',marker='*',color='green')
  plt.scatter(df.index,df['sell'],alpha=1,label='sellsignal',marker='*',color='red')

  plt.xticks(rotation=45)
  plt.show()