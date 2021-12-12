from flask import Flask, jsonify, render_template, request
from yahoo_fin.stock_info import get_data
import numpy as np
import pandas as pd
from sma30 import sma30 
from macd import macd_
from fibonacci import fibanocii
import requests
import time
app = Flask(__name__)


@app.route('/urlapi',methods=['GET','POST'])
def url_rep():
      value = request.args.get('dmk')
      value=value.upper()
      api_secret = 'c654b02b275e45e0333b40b76286a91a'
      api_key = 'acc_7b4791ea506b6bf'
      r = requests.get('https://finnhub.io/api/v1/stock/recommendation?symbol='+value+'&token=c6qpil2ad3i891nj69r0')
      if r.status_code == 200:
         data = r.json()
         quote = f'<br><b>Buy :</b> {data[0]["buy"]} <br> <b>hold :</b> {data[0]["hold"]}<br><b> Sell :</b> {data[0]["sell"]}<br><b> Strong-Buy :</b> {data[0]["strongBuy"]} <br><b> Strong-Selll : </b>{data[0]["strongSell"]} '
      else:
         quote = 'Server Error'
      return {"fruit":value,"details":quote}
   

@app.route('/strat',methods=['GET','POST'])
def strati():
      value = request.args.get('dmk')
      sd = request.args.get('sd')
      ed = request.args.get('ed')
      x = request.args.get('strat')
      value=value.upper()
      #get stock data, start date and end date
      data= get_data(value, start_date=sd, end_date=ed, index_as_date = True, interval="1d")


      # get wat type of strategy (sma30 , macd , fibanocci)
      if x=="sma30":
         sma30(data) 
         
      if x=="macd":
         macd_(data)
         
      if x=="fibbo":
         fibanocii(data)
         
      # print("strateggggggy "+x)
      return {"fruit":"ff","details":"dd"}

@app.route('/')
def homescan():
   return render_template('index.html')

@app.route('/trading')
def urlscaning():
   return render_template('index.html')



@app.route('/Strategies')
def dnsipscaning():
   return render_template('dietplan.html')

if __name__ == '__main__':
   app.run()