# generator.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from strategy import get_top_strategies
from backtest import run_backtest
import time


def backtest_generator(price_df, selected_stocks, step=0.25):
    top10 = get_top_strategies(price_df, selected_stocks, step, top_n=10)

    for idx, row in top10.iterrows():
        cumret = row["CumReturn"]
        cagr = row["CAGR"]
        sharpe = row["Sharpe"]
        mdd = row["Max Drawdown"]

        for i in range(len(cumret)):
            fig, ax = plt.subplots()
            ax.plot(cumret.index[:i+1], cumret.values[:i+1], color="blue")
            ax.set_title(f"Cumulative Return (Strategy {idx+1})")
            ax.set_xlabel("Date")
            ax.set_ylabel("Cumulative Return")
            ax.set_xlim(cumret.index[0], cumret.index[-1])
            ax.set_ylim(cumret.min()*0.95, cumret.max()*1.05)
            plt.close(fig)

            cum_return_now = cumret.values[i]
            cagr_text = f"CAGR: {cagr:.4f}"
            sharpe_text = f"Sharpe: {sharpe:.4f}"
            mdd_text = f"Max Drawdown: {mdd:.4f}"
            info_text = f"Cumulative Return: {cum_return_now:.4f}\n{cagr_text}\n{sharpe_text}\n{mdd_text}"

            yield fig, info_text, idx+1
            time.sleep(0.05)  # 动画间隔
