import pandas as pd
import numpy as np
from itertools import product

# -------------------------------
# 1️⃣ 读取价格数据
# -------------------------------
prices = pd.read_csv("data/data.csv", parse_dates=["Date"])
prices.set_index("Date", inplace=True)

# -------------------------------
# 2️⃣ 定义股票、操作和权重
# -------------------------------
stocks = prices.columns.tolist()
actions = ["Buy", "Skip"]
weights_options = [0.3, 0.5, 0.7]  # 买入权重选择

# -------------------------------
# 3️⃣ 生成笛卡尔积策略组合
# -------------------------------
action_combos = list(product(actions, repeat=len(stocks)))
weight_combos = list(product(weights_options, repeat=len(stocks)))

strategies = []
for act in action_combos:
    if "Buy" not in act:
        continue  # 至少买一只股票
    for w in weight_combos:
        # 只给买入股票分配权重
        w_arr = np.array([wi if a == "Buy" else 0 for wi, a in zip(w, act)])
        if w_arr.sum() == 0:
            continue
        w_arr = w_arr / w_arr.sum()  # 归一化权重
        strategies.append({"Action": act, "Weights": tuple(w_arr)})

# 去重策略
unique_strategies = []
seen = set()
for s in strategies:
    key = (s["Action"], s["Weights"])
    if key not in seen:
        seen.add(key)
        unique_strategies.append(s)
strategies = unique_strategies

print(f"总策略数: {len(strategies)}")

# -------------------------------
# 4️⃣ 回测函数
# -------------------------------


def backtest_strategy(prices, stocks, action, weights):
    selected_stocks = [s for s, a in zip(stocks, action) if a == "Buy"]
    if not selected_stocks:
        return None

    returns = prices[selected_stocks].pct_change().dropna()
    weights_arr = np.array([w for s, w, a in zip(
        stocks, weights, action) if a == "Buy"])
    portfolio_returns = returns.dot(weights_arr)

    # 累计收益
    cumulative_return = (1 + portfolio_returns).cumprod()

    # CAGR
    n_days = (cumulative_return.index[-1] - cumulative_return.index[0]).days
    n_years = n_days / 365.0
    cagr = cumulative_return.iloc[-1]**(1/n_years) - 1

    # 年化夏普比率
    mean_ret = portfolio_returns.mean() * 252
    vol_ret = portfolio_returns.std() * np.sqrt(252)
    sharpe = mean_ret / vol_ret if vol_ret != 0 else np.nan

    # 最大回撤
    cum_max = cumulative_return.cummax()
    drawdown = (cumulative_return - cum_max) / cum_max
    max_dd = drawdown.min()

    return {
        "Action": action,
        "Weights": weights,
        "CAGR": cagr,
        "Sharpe": sharpe,
        "Max Drawdown": max_dd,
        "Cumulative Return": cumulative_return
    }


# -------------------------------
# 5️⃣ 批量回测
# -------------------------------
results = []
for strat in strategies:
    res = backtest_strategy(prices, stocks, strat["Action"], strat["Weights"])
    if res:
        results.append(res)

# -------------------------------
# 6️⃣ 生成指标表
# -------------------------------
summary = pd.DataFrame([{
    "Action": r["Action"],
    "Weights": r["Weights"],
    "CAGR": r["CAGR"],
    "Sharpe": r["Sharpe"],
    "Max Drawdown": r["Max Drawdown"]
} for r in results])

summary = summary.sort_values("Sharpe", ascending=False).reset_index(drop=True)
print(summary.head(10))  # 输出前10个策略
