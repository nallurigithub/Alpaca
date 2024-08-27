# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 08:30:13 2024

@author: nagar nvidia 22july, 3rd july
"""

from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from alpaca.data.historical import StockHistoricalDataClient
from datetime import datetime, time, timedelta
import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st


#Define the Alpaca keys
api_key = "PKQJGFL6CHBQO5F2866J"
api_secret = "4r4lJ1eHXfXZ6HwjqZmuFZYhaewuKccKHFz60Mum"
client = StockHistoricalDataClient(api_key, api_secret)


#Set the APi Parameters
now = datetime.now()
endday = now.replace(hour=0, minute=0, second=0, microsecond=0)
endday = endday - timedelta(days=127);
#print(endday)
startdate= endday - timedelta(days=50)
request_params = StockBarsRequest(
                        symbol_or_symbols=['NVDA','AAPL','TSLA','MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD', 'ABNB', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ACGL', 'ADM', 'ANET', 'AJG', 'AIZ', 'T', 'ATO','ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'AXON', 'BKR', 'BALL', 'BAC', 'BK', 'BBWI', 'BAX', 'BDX', 'BRK.B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BX', 'BA', 'BKNG', 'BWA', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BF.B', 'BLDR', 'BG', 'BXP', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'COR', 'CNC', 'CNP', 'CF', 'CHRW', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CPAY', 'CTVA', 'CSGP', 'COST', 'CTRA', 'CRWD', 'CCI', 'CSX', 'CMI', 'CVS', 'DHR', 'DRI', 'DVA', 'DAY', 'DECK', 'DE', 'DAL', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DHI', 'DTE', 'DUK', 'DD', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'ELV', 'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'EG', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FICO', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FI', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'FCX', 'GRMN', 'IT', 'GE', 'GEHC', 'GEV', 'GEN', 'GNRC', 'GD', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GDDY', 'GS', 'HAL', 'HIG', 'HAS', 'HCA', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 'ITW', 'INCY', 'IR', 'PODD', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'INVH', 'IQV', 'IRM', 'JBHT', 'JBL', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KKR', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LLY', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LULU', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'META', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'MOH', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'ON', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PANW', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 'PEP', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PTC', 'PSA', 'PHM', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RVTY', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SJM', 'SW', 'SNA', 'SOLV', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STLD', 'STE', 'SYK', 'SMCI', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TRGP', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 'USB', 'UBER', 'UDR', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO', 'VTR', 'VLTO', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VTRS', 'VICI', 'V', 'VST', 'VMC', 'WRB', 'GWW', 'WAB', 'WBA', 'WMT', 'DIS', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WY', 'WMB', 'WTW', 'WYNN', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZTS',
],
                        timeframe=TimeFrame.Day,
                        start=startdate, end=endday
                 )

#Make APi call
bars_df = client.get_stock_bars(request_params).df;
bars_df['EMA_50'] = bars_df['close'].ewm(span=50, adjust=False).mean()
bars_df['EMA_5'] = bars_df['close'].ewm(span=5, adjust=False).mean()
bars_df = bars_df.reset_index()  
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(bars_df)

#Read only latest 3 days data
top_3_rows_per_group = bars_df[bars_df['timestamp'] > (bars_df['timestamp'].max() - pd.Timedelta(days=3))]
#print(top_3_rows_per_group)
top_3_rows_per_group.to_csv('output.csv', index=False)
grouped = top_3_rows_per_group.groupby('symbol')


# Function to validate each group
def validate_rule1(group):
    
        
    candle0_date = group['timestamp'].max().date()    
    candle0_day_rows = group[group['timestamp'].dt.date == candle0_date]    
    
    candleMinus1_date = (group['timestamp'].max() - pd.Timedelta(days=1)).date()
    candleMinus1_day_rows = group[group['timestamp'].dt.date == candleMinus1_date]
    
        
    candleMinus2_date = (group['timestamp'].max() - pd.Timedelta(days=2)).date()
    candleMinus2_day_rows = group[group['timestamp'].dt.date == candleMinus2_date]
    
    
    for index, current_row_Minus0 in candle0_day_rows.iterrows():
             
        current_row_Minus1 = candleMinus1_day_rows.loc[(candleMinus1_day_rows['timestamp'] == (current_row_Minus0['timestamp']- pd.Timedelta(days=1)))]
        current_row_Minus2 = candleMinus2_day_rows.loc[(candleMinus2_day_rows['timestamp'] == (current_row_Minus0['timestamp']- pd.Timedelta(days=2)))]
       
        
        #if current_row_Minus0['close'] > current_row_Minus0['EMA_5'] and current_row_Minus0['open'] < current_row_Minus0['EMA_5'] and current_row_Minus0['volume'] > current_row_Minus1['volume'].any():
        if current_row_Minus0['close'] > current_row_Minus0['EMA_5'] and current_row_Minus0['open'] < current_row_Minus0['EMA_5'] and current_row_Minus0['volume'] > current_row_Minus1['volume'].any():
            
            if current_row_Minus1['high'].any() < current_row_Minus1['EMA_5'].any() and current_row_Minus1['high'] < current_row_Minus2['high'] and current_row_Minus1['low'] > current_row_Minus2['low']:
            
                return True;
               
           
    return False
            
   
    
st.header("  :blue[Alpaca Trade Data]")



#apply ruule 1
validation_results = grouped.apply(validate_rule1)
#st.table(validation_results)
# Generate an HTML table with custom headers
html_table = '<table ><tr style="background:silver"><th>Symbol</th><th>Is Rule1 Passed</th></tr>'

for key, value in validation_results.items():
    html_table += f'<tr><td>{key}</td><td>{value}</td></tr>'

html_table += '</table>'

# Display the HTML table
st.write(html_table, unsafe_allow_html=True)






#st.markdown("<style>th { color: blue; }</style>", unsafe_allow_html=True)
#st.markdown(validation_results.to_html(render_links=True), unsafe_allow_html=True)

#for key, value in validation_results.items():   
        #print(f"{key}: {value}")
#print(type(validation_results))
    





