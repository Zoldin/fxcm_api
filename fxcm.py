import fxcmpy
import pandas as pd
import datetime as dt
import time
import numpy as np
import decimal
import mysql.connector

#token provided from fxcm 
token =''
con = fxcmpy.fxcmpy(access_token = token, log_level = 'error')
instruments = con.get_instruments()

#initialize start date and end date
start = dt.datetime(2018, 7,1)
stop = dt.datetime(2018,7 15)
#use get_candles methos for accessing data from fxcm
prices = con.get_candles('EUR/USD', period='m1',start=start, stop=stop)

prices.rename(columns = {'askopen':'open', 'askhigh':'high', 'asklow':'low','askclose':'close'}, inplace = True) 
ctm = prices.index.astype(np.int64)//10**9
prices = prices.assign(ctm=ctm)
prices = prices.assign(ctm_dtm=cijene.index)

#use pymysql package for data load (into mysql aws rds database)

import pymysql
#connection credentials
user=''
password=''
ip=''
from sqlalchemy import create_engine

engine = create_engine( 'mysql+pymysql://' + user + ':' + password + '@' + ip + ':3306/shema_name')

#load the prices into the database
prices[['ctm_dtm','ctm','open','low','high','close']][:-1].to_sql(name='OHLC_GBPUSD_HIST', con=engine, if_exists = 'append', index=False)
