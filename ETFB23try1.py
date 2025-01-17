#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
#from PIL import Image
#import pandas_datareader as web
import datetime as dt
import yfinance as yf


# In[7]:


st.write("""
# ETF Builder
** Custom Price Weighted Index using Streaminglit 
""")
st.sidebar.header('User Input')
start_date = st.sidebar.text_input("Start Date", "2020-01-01")
end_date = st.sidebar.text_input("End Date", "2025-01-01")
stock_symbols = st.sidebar.text_input("Stock Symbol", "AMD, SNAP")
tickers = [x for x in stock_symbols.split(', ')]
#print(List)

start = dt.datetime.strptime(start_date, '%Y-%m-%d')
end = dt.datetime.strptime(end_date, '%Y-%m-%d')

ETF = pd.DataFrame()
for tick in tickers:
#  df2 = web.DataReader(tick,'yahoo',start,end)
    df2 = yf.download(tick, start, end)
    ETF[tick] = df2['Close']
ETF['Sum'] = ETF.sum(axis = 1)
ETF['Average'] = ETF['Sum'] / len(tickers)
print (ETF.tail())


#df = web.DataReader(stock_symbol.upper(),'yahoo', start, end)
#df.tail()


# In[8]:


st.header("Price Weighted Average\n")
st.line_chart(ETF['Average'])


# In[ ]:





# In[ ]:




