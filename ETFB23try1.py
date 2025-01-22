#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import datetime as dt
import yfinance as yf

st.write("""
# ETF Builder
**Custom Market Weighted Index using Streamlit**
""")

# Sidebar inputs for user
st.sidebar.header('User Input')
start_date = st.sidebar.text_input("Start Date", "2020-01-01")
end_date = st.sidebar.text_input("End Date", "2025-01-01")
#stock_symbols = st.sidebar.text_input("Stock Symbols (comma-separated)", "AMD, SNAP")


#tickers = [x.strip() for x in stock_symbols.split(',')]

stock_symbols = st.sidebar.text_input("Stock Symbols", " GM F RACE TSLA")  # Flexible input
tickers = [x.strip().upper() for x in stock_symbols.replace(',', ' ').split()]

start = dt.datetime.strptime(start_date, '%Y-%m-%d')
end = dt.datetime.strptime(end_date, '%Y-%m-%d')

# Dataframe to hold ETF data
ETF = pd.DataFrame()

# Fetch data and calculate market cap weights
weights = {}
total_market_cap = 0

for tick in tickers:
    # Fetch stock data
    stock_data = yf.Ticker(tick)

    df = stock_data.history(start=start_date, end=end_date)
    
    # Get closing prices
    ETF[tick] = df['Close']
    
    # Get market cap
   # try:
   #     market_cap = stock_data.info['marketCap']
   #     weights[tick] = market_cap
   #     total_market_cap += market_cap
   # except KeyError:
   #     st.error(f"Market cap not found for {tick}. Please check the ticker symbol.")
   #     weights[tick] = 0

# Normalize weights
for tick in weights:
    weights[tick] = weights[tick] / total_market_cap if total_market_cap > 0 else 0

# Display stock prices (each line in a different color)
st.header("Individual Stock Prices")
st.line_chart(ETF[tickers])

# Calculate Market Weighted Index
#ETF['Weighted Sum'] = sum(ETF[tick] * weights[tick] for tick in tickers)
#ETF['Market Weighted Index'] = ETF['Weighted Sum'] / sum(weights.values())

# Calculate Dollar-Weighted Average (similar to DOW)
ETF['Dollar Weighted Average'] = ETF[tickers].mean(axis=1)

# Display results
st.header("Market Weighted Index")
st.line_chart(ETF['Market Weighted Index'])
st.header("Dollar Weighted Average")
st.line_chart(ETF['Dollar Weighted Average'])
st.dataframe(ETF.tail())



# In[ ]:




