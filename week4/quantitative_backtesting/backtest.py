# backtest.py
import numpy as np
import pandas as pd


def run_backtest(price_df: pd.DataFrame, weights: np.ndarray):
    """
    简单的组合回测
    price_df: 每列为一只股票的历史价格，索引为日期
    weights: 权重数组，长度必须等于股票数量，和为1
    """
    # 计算日收益率
    returns = price_df.pct_change().dropna()

    # 组合每日收益
    portfolio_returns = returns.dot(weights)

    # 累计收益
    cum_return = (1 + portfolio_returns).cumprod()
    cum_return.name = "CumReturn"

    # 年化收益 (CAGR)
    n_days = len(cum_return)
    cagr = (cum_return.iloc[-1]) ** (252 / n_days) - 1

    # 年化波动率
    ann_vol = portfolio_returns.std() * np.sqrt(252)

    # 夏普比率 (假设无风险利率=0)
    sharpe = cagr / ann_vol if ann_vol != 0 else 0

    # 最大回撤
    rolling_max = cum_return.cummax()
    drawdown = (cum_return - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    return {
        "CAGR": cagr,
        "Sharpe": sharpe,
        "Max Drawdown": max_drawdown,
        "CumReturn": cum_return
    }
