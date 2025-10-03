import pandas as pd
import numpy as np


def run_backtest(price_data, portfolio):
    prices = price_data[list(portfolio)].copy()
    returns = prices.pct_change().dropna()
    weights = np.array([1 / len(portfolio)] * len(portfolio))
    portfolio_returns = returns.dot(weights)
    cumulative_return = (1 + portfolio_returns).cumprod()
    sharpe = portfolio_returns.rolling(window=20).mean(
    ) / portfolio_returns.rolling(window=20).std()
    sharpe = sharpe.fillna(0)
    cum_max = cumulative_return.cummax()
    drawdown = (cumulative_return - cum_max) / cum_max
    max_drawdown = drawdown.cummin()
    result = pd.DataFrame({
        "Date": cumulative_return.index,
        "Cumulative Return": cumulative_return.values,
        "Sharpe": sharpe.values,
        "Max Drawdown": max_drawdown.values
    })
    return result
