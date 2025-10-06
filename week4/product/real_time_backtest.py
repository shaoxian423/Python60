# real_time_backtest_5y.py
import pandas as pd
import numpy as np
from datetime import datetime

DATA_FILE = "data/data.csv"


def read_prices_generator(file_path):
    """生成器：逐行读取价格数据"""
    df = pd.read_csv(file_path, parse_dates=["Date"])
    for idx, row in df.iterrows():
        prices = row.drop("Date").to_dict()
        yield row["Date"], prices


def run_backtest(prices_gen, initial_cash=1.0):
    """逐行回测生成器数据"""
    cum_returns = []
    prev_prices = None
    portfolio_value = initial_cash
    for date, prices in prices_gen:
        if prev_prices is None:
            # 首日初始化
            cum_returns.append(portfolio_value)
        else:
            # 简单等权组合收益计算
            tickers = list(prices.keys())
            daily_ret = np.mean([
                (prices[t] - prev_prices[t]) / prev_prices[t] for t in tickers
            ])
            portfolio_value *= (1 + daily_ret)
            cum_returns.append(portfolio_value)
        prev_prices = prices
        print(f"{date.date()} -> Prices: {prices} | CumReturn: {portfolio_value:.4f}")
    cum_returns = np.array(cum_returns)

    # 精确年化指标
    n_years = (len(cum_returns) / 252)  # 按交易日计算年份
    cagr = cum_returns[-1] ** (1 / n_years) - 1
    daily_returns = np.diff(cum_returns) / cum_returns[:-1]
    sharpe = np.mean(daily_returns) / np.std(daily_returns) * np.sqrt(252)
    cum_max = np.maximum.accumulate(cum_returns)
    drawdown = (cum_returns - cum_max) / cum_max
    max_drawdown = drawdown.min()

    summary = {
        "CAGR": cagr,
        "Sharpe": sharpe,
        "Max Drawdown": max_drawdown
    }
    return summary


if __name__ == "__main__":
    prices_gen = read_prices_generator(DATA_FILE)
    summary = run_backtest(prices_gen)
    print("\n=== 回测汇总 (5 年数据) ===")
    print(summary)
