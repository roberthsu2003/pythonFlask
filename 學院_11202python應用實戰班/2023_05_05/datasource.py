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
    return stock_dataFrame