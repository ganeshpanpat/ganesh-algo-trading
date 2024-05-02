import streamlit as st
from streamlit.logger import get_logger
import yfinance as yf
import datetime
import time
from dateutil.tz import gettz
import pandas as pd
LOGGER = get_logger(__name__)
st.set_page_config(page_title="Algo App",layout="wide",initial_sidebar_state="expanded",)
st.markdown("""
  <style>
    .block-container {padding-top: 0.5rem;padding-bottom: 0rem;padding-left: 2rem;padding-right: 5rem;}
  </style>
  """, unsafe_allow_html=True)
st.write("# Welcome to My Algo!")
start=st.button("Start")
order_book_updated=st.empty()
order_book_updated.text(f"Orderbook : ")
order_datatable=st.empty()

def get_yf_data(symbol,interval):
  df=yf.Ticker(symbol).history(interval=interval,period=str(2)+"d")
  df['Datetime'] = df.index
  df['Datetime']=df['Datetime'].dt.tz_localize(None)
  df.index=df['Datetime']
  df=df[['Datetime','Open','High','Low','Close','Volume']]
  df['Date']=df['Datetime'].dt.strftime('%m/%d/%y')
  df['Datetime'] = pd.to_datetime(df['Datetime']).dt.time
  df['Symbol']=symbol
  df=df[['Symbol','Date','Datetime','Open','High','Low','Close','Volume']]
  
  df=df.round(2)
  return df.tail(1)
def sub_loop(interval=5):
  df=pd.DataFrame()
  for symbol in ['^NSEI','^NSEBANK','^BSESN']:
    yf_data=get_yf_data(symbol,str(interval)+"m")
    df=pd.concat([df,yf_data])
  return df
def run():
  for i in range(100):
    df=sub_loop(5)
    order_datatable.dataframe(df,hide_index=True)
    order_book_updated.text(f"Orderbook : {datetime.datetime.now(tz=gettz('Asia/Kolkata')).time().replace(microsecond=0)}")
    time.sleep(60)
if start==True:
  run()

