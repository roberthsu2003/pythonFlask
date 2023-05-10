'''
這是專門取得台灣股市資料
'''
import pandas_datareader.data as pdr
import yfinance as yf
import os
from datetime import datetime

def get_stock_data(stockid):
    '''
    @parma stockid是股票代碼
    '''
    yf.pdr_override()
    stockid_str = f'{stockid}.TW'   
    current = os.path.abspath("./")
    current_date = datetime.now()    
    filename = f"{stockid_str}_{current_date.year}_{current_date.month}_{current_date.day}.csv"
    csv_file_path = os.path.join(current,'data',filename)
    if not os.path.exists(csv_file_path):
        stock_dataFrame = pdr.get_data_yahoo(stockid_str)
        stock_dataFrame.to_csv(csv_file_path)
    else:
        print("讀取檔案")
    
    stock_dataFrame1 = stock_dataFrame.reset_index()
    stock_dataFrame1['Date'] = stock_dataFrame1['Date'].map(lambda x:f'{x.year}-{x.month}-{x.day}')
    stock_list = stock_dataFrame1.to_numpy().tolist()
    return stock_list