import gradio as gr
import pandas as pd
import yfinance as yf
from trade_portfolio import load_trades, calculate_portfolio, get_portfolio_summary
import plotly.express as px

# 加载交易记录
trades = load_trades()

# 获取所有股票代码
stocks = sorted(trades['stock'].unique())

# 获取实时市场价格


def get_market_prices(stocks):
    prices = {}
    for s in stocks:
        try:
            ticker = yf.Ticker(s)
            prices[s] = ticker.history(period="1d")['Close'].iloc[-1]
        except Exception as e:
            prices[s] = 0  # 出错时默认价格为0
    return prices

# 更新投资组合


def update_portfolio():
    market_price = get_market_prices(stocks)
    portfolio = calculate_portfolio(trades)
    summary = get_portfolio_summary(portfolio, market_price)
    df = pd.DataFrame(summary)

    # 饼图：持仓占比
    pie_fig = px.pie(df, names='Stock', values='Portfolio %',
                     title='Portfolio %')

    # 条形图：盈亏
    bar_fig = px.bar(df, x='Stock', y='Gain/Loss', title='Gain/Loss per Stock')

    return df, pie_fig, bar_fig


# Gradio 界面
with gr.Blocks() as demo:
    gr.Markdown("## 📊 Real-Time Stock Portfolio Dashboard")

    update_btn = gr.Button("Refresh Portfolio")

    portfolio_table = gr.Dataframe(
        headers=["Stock", "Quantity", "Market Value", "Gain/Loss",
                 "Average Cost", "Book Cost", "Portfolio %"],
        datatype=["str", "number", "number",
                  "number", "number", "number", "number"]
    )
    pie_chart = gr.Plot()
    bar_chart = gr.Plot()

    update_btn.click(
        fn=update_portfolio,
        inputs=[],
        outputs=[portfolio_table, pie_chart, bar_chart]
    )

demo.launch()
