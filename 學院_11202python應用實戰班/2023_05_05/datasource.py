'''
這是專門取得台灣股市資料
'''
import pandas_datareader.data as pdr
import yfinance as yf

def get_stock_data(stockid):
    '''
    @parma stockid是股票代碼
    '''
    yf.pdr_override()
    stockid_str = f'{stockid}.TW'    
    stock_dataFrame = pdr.get_data_yahoo(stockid_str)
    stock_dataFrame1 = stock_dataFrame.reset_index()
    stock_dataFrame1['Date'] = stock_dataFrame1['Date'].map(lambda x:f'{x.year}-{x.month}-{x.day}')
    stock_list = stock_dataFrame1.to_numpy().tolist()
    return stock_list