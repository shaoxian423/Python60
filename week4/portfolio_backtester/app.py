import gradio as gr
import pandas as pd
import plotly.express as px
from datetime import datetime
from fetch_data import get_prices
from portfolio import generate_combinations
from backtest import run_backtest

# 自动获取今天日期
today = datetime.today().strftime("%Y-%m-%d")


def backtest_interface(stocks, start_date, end_date, comb_size):
    stocks = [s.strip().upper() for s in stocks.split(",") if s.strip()]
    if len(stocks) < comb_size:
        return pd.DataFrame(), None

    # 获取价格数据（缓存到 data/）
    prices = get_prices(stocks, start_date, end_date)
    if prices.empty:
        return pd.DataFrame(), None

    # 生成组合
    combs = generate_combinations(stocks, comb_size)

    # 回测每个组合
    results = []
    for comb in combs:
        df = run_backtest(prices, comb)
        results.append({
            "Portfolio": ",".join(comb),
            "Return": df["Cumulative Return"].iloc[-1],
            "Sharpe": df["Sharpe"].iloc[-1],
            "Max Drawdown": df["Max Drawdown"].iloc[-1],
            "Cumulative Data": df
        })

    res_df = pd.DataFrame(results).sort_values("Return", ascending=False)

    # 可视化前3组合
    fig = px.line()
    top_n = min(3, len(res_df))
    for i in range(top_n):
        comb = res_df.iloc[i]["Portfolio"].split(",")
        cum_df = res_df.iloc[i]["Cumulative Data"]
        fig.add_scatter(
            x=cum_df["Date"],
            y=cum_df["Cumulative Return"],
            mode='lines',
            name=f"Top {i+1}: {','.join(comb)}"
        )

    fig.update_layout(title="Top 3 Portfolio Cumulative Returns",
                      xaxis_title="Date", yaxis_title="Cumulative Return")

    return res_df.drop(columns=["Cumulative Data"]), fig


# Gradio 前端
with gr.Blocks() as demo:
    gr.Markdown("## 📊 Portfolio Backtester (Gradio Edition)")

    with gr.Row():
        stocks_input = gr.Textbox(
            label="Stock List (comma separated)",
            value="AAPL,MSFT,TSLA,GOOG,AMZN"  # 默认5支股票
        )
        start_date = gr.Textbox(label="Start Date", value="2020-01-01")
        end_date = gr.Textbox(label="End Date", value=today)
        comb_size = gr.Slider(2, 5, value=3, step=1, label="Portfolio Size")

    run_btn = gr.Button("Run Backtest")
    results_table = gr.Dataframe(
        headers=["Portfolio", "Return", "Sharpe", "Max Drawdown"]
    )
    chart = gr.Plot()

    run_btn.click(
        fn=backtest_interface,
        inputs=[stocks_input, start_date, end_date, comb_size],
        outputs=[results_table, chart]
    )

demo.launch()
