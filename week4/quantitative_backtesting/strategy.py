# strategy.py
import itertools
import numpy as np
import pandas as pd
from backtest import run_backtest


def generate_weight_combinations(n_stocks, step=0.25):
    steps = np.arange(0, 1 + step, step)
    all_combs = [c for c in itertools.product(
        steps, repeat=n_stocks) if abs(sum(c) - 1) < 1e-6]
    return all_combs


def get_top_strategies(price_df: pd.DataFrame, selected_stocks: list, step=0.25, top_n=10):
    n = len(selected_stocks)
    weight_combs = generate_weight_combinations(n, step)
    summary = []

    for w in weight_combs:
        sub_prices = price_df[selected_stocks]
        res = run_backtest(sub_prices, np.array(w))
        summary.append({
            "Weights": w,
            "CAGR": res["CAGR"],
            "Sharpe": res["Sharpe"],
            "Max Drawdown": res["Max Drawdown"],
            "CumReturn": res["CumReturn"]
        })

    df = pd.DataFrame(summary)
    df = df.sort_values("Sharpe", ascending=False).reset_index(drop=True)
    return df.head(top_n)
