# Raw packages
import numpy as np
import pandas as pd

# Data Source 
import yfinance as yf 

# Data visualization
import plotly.graph_objs as go

# Get Bitcoin data (period: 1m , 1h, 1d, 1wk, 1mo)
data = yf.download(tickers='BTC-EUR', period = '10d', interval = '1h')

#declare figure
fig = go.Figure()

#Candlestick
fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

# Add titles
fig.update_layout(
    title='Grafico evoluzione prezzo bitcoin',
    yaxis_title='Bitcoin Price (kEUR Euros)')

# X-Axes
fig.update_xaxes(
    tickmode = 'linear',
    tick0 = 10,
    # dtick = 0.75,
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=6, label="6h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)


#Show
fig.show()