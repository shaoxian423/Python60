import yfinance as yf
import pandas as pd
import os
from datetime import datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


def get_prices(stocks, start_date, end_date=None):
    """
    获取历史收盘价（参考实时仪表盘方式，但保留批量下载）
    stocks: ['AAPL', 'MSFT', ...]
    start_date: 'YYYY-MM-DD'
    end_date: 'YYYY-MM-DD'，默认今天
    返回: DataFrame，列为股票代码，索引为日期
    """
    if not end_date:
        end_date = datetime.today().strftime("%Y-%m-%d")

    tickers_str = "_".join(stocks)
    cache_file = os.path.join(
        DATA_DIR, f"{tickers_str}_{start_date}_{end_date}.csv")

    # 先看缓存
    if os.path.exists(cache_file):
        return pd.read_csv(cache_file, index_col=0, parse_dates=True)

    # 批量下载
    raw = yf.download(stocks, start=start_date, end=end_date, auto_adjust=True)

    # 处理 MultiIndex
    if isinstance(raw.columns, pd.MultiIndex):
        if 'Adj Close' in raw.columns.get_level_values(0):
            data = raw['Adj Close'].copy()
        elif 'Close' in raw.columns.get_level_values(0):
            data = raw['Close'].copy()
        else:
            # fallback: 取第一层所有列
            data = raw.iloc[:, :len(stocks)]
        data.columns = stocks
    else:
        # 单支股票
        if 'Adj Close' in raw.columns:
            data = raw[['Adj Close']].copy()
        else:
            data = raw[['Close']].copy()
        data.columns = stocks

    data = data.dropna(how='all')
    data.to_csv(cache_file)
    return data


# 测试
if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]
    df = get_prices(tickers, "2023-01-01")
    print(df.head())
