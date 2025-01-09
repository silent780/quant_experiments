'''
@File    :   usa_pe.py
@Time    :   2025/01/09 10:40:43
@Author  :   glx 
@Version :   1.0
@Contact :   18095542g@connect.polyu.hk
@Desc    :   get latest PE ratio of USA market use S&P500 index, Dow Jones Index, Nasdaq Index 
'''

# here put the import lib
'''
@File    :   usa_pe.py
@Time    :   2025/01/09 10:40:43
@Author  :   glx
@Version :   1.0
@Contact :   18095542g@connect.polyu.hk
@Desc    :   get latest PE ratio of USA market use S&P500 index, Dow Jones Index, Nasdaq Index
'''

# here put the import lib
import yfinance as yf
import pandas as pd

def get_index_tickers_sp500():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    df = None
    for t in tables:
        if 'Symbol' in t.columns:
            df = t
            break
    if df is None:
        return []
    return df["Symbol"].tolist()

def get_index_tickers_dow():
    url = "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average"
    tables = pd.read_html(url)
    df = None
    for t in tables:
        if 'Symbol' in t.columns:
            df = t
            break
    if df is None:
        return []
    return df["Symbol"].tolist()

def get_index_tickers_nasdaq100():
    url = "https://en.wikipedia.org/wiki/Nasdaq-100"
    tables = pd.read_html(url)
    df = None
    for t in tables:
        if 'Symbol' in t.columns:
            df = t
            break
    if df is None:
        return []
    return df["Symbol"].tolist()

def get_average_pe(tickers):
    pe_values = []
    for t in tickers:
        try:
            info = yf.Ticker(t).info
            pe = info.get("trailingPE", None) or info.get("forwardPE", None)
            if pe and pe > 0:
                pe_values.append(pe)
        except Exception:
            pass
    return sum(pe_values)/len(pe_values) if pe_values else None

if __name__ == "__main__":
    sp500_tickers = get_index_tickers_sp500()
    dow_tickers = get_index_tickers_dow()
    nasdaq100_tickers = get_index_tickers_nasdaq100()

    sp500_pe = get_average_pe(sp500_tickers)
    dow_pe = get_average_pe(dow_tickers)
    nasdaq_pe = get_average_pe(nasdaq100_tickers)

    print("S&P 500平均PE:", sp500_pe)
    print("Dow 30平均PE:", dow_pe)
    print("Nasdaq 100平均PE:", nasdaq_pe)