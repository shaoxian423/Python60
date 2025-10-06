# real_time_backtest_generator.py

import pandas as pd
import numpy as np

# -----------------------------
# 生成器：逐行读取 CSV（模拟日志或实时行情流）
# -----------------------------


def read_prices_generator(csv_path):
    for row in pd.read_csv(csv_path).itertuples(index=False):
        prices = {
            "AAPL": row.AAPL,
            "MSFT": row.MSFT,
            "TSLA": row.TSLA,
            "GOOG": row.GOOG,
            "AMZN": row.AMZN
        }
        yield row.Date, prices


# -----------------------------
# 简单等权组合回测函数
# -----------------------------
def simple_backtest(prices_dict_list):
    """prices_dict_list: [(date, prices), ...]"""
    cum_return = 1.0
    cum_returns = []
    for date, prices in prices_dict_list:
        # 等权组合收益
        weights = np.array([1/len(prices)]*len(prices))
        daily_return = np.dot(list(prices.values()), weights) / \
            np.dot(list(prices.values())[0:1], [1]) - 1
        cum_return *= (1 + daily_return)
        cum_returns.append((date, cum_return))
    return cum_returns


# -----------------------------
# 实时回测模拟
# -----------------------------
def run_real_time_backtest(csv_path):
    print("=== Starting Real-Time Backtest ===")
    generator = read_prices_generator(csv_path)
    cum_return = 1.0

    for idx, (date, prices) in enumerate(generator, start=1):
        # 简单日收益率：等权组合
        weights = np.array([1/len(prices)]*len(prices))
        daily_return = np.dot(list(prices.values()), weights) / \
            np.mean(list(prices.values())) - 1
        cum_return *= (1 + daily_return)
        print(f"{idx}: {date} -> Prices: {prices} | CumReturn: {cum_return:.4f}")


# -----------------------------
# 测试运行
# -----------------------------
if __name__ == "__main__":
    csv_path = "data/data.csv"  # 你的5年价格数据
    run_real_time_backtest(csv_path)
