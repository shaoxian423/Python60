import gradio as gr
import pandas as pd
import plotly.graph_objects as go
import time
from strategy import generate_weight_combinations
from backtest import run_backtest

# ================================
# 数据加载
# ================================
prices = pd.read_csv("data/data.csv", index_col="Date", parse_dates=True)
stock_list = list(prices.columns)
cached_top10 = None


# ================================
# 回测逻辑
# ================================
def backtest_ui(selected_stocks, step=0.25):
    global cached_top10
    if not selected_stocks:
        return None, None, "", gr.update(choices=[]), gr.update(maximum=0, value=0)

    selected_prices = prices[selected_stocks]
    n = len(selected_stocks)
    weight_combs = generate_weight_combinations(n, step=step)

    summary_list = []
    for w in weight_combs:
        res = run_backtest(selected_prices, w)
        summary_list.append({
            "Weights": w,
            "CAGR": res["CAGR"],
            "Sharpe": res["Sharpe"],
            "Max Drawdown": res["Max Drawdown"],
            "CumReturn": res["CumReturn"]
        })

    summary_df = pd.DataFrame(summary_list)
    summary_df = summary_df.sort_values(
        "Sharpe", ascending=False).reset_index(drop=True)
    top10 = summary_df.head(10)
    cached_top10 = top10

    top10_display = top10.copy()
    top10_display["Weights"] = top10_display["Weights"].apply(
        lambda x: [f"{v:.2f}" for v in x])
    top10_display = top10_display.drop(columns=["CumReturn"])

    choices = [f"Strategy {i+1}" for i in range(len(top10))]
    slider_max = len(cached_top10.iloc[0]["CumReturn"]) - 1

    return top10_display, make_plot("Strategy 1", 0), "", gr.update(choices=choices, value=choices[0]), gr.update(maximum=slider_max, value=0)


# ================================
# 绘图函数
# ================================
def make_plot(strategy_name, date_index):
    if cached_top10 is None or strategy_name is None:
        return go.Figure()

    idx = int(strategy_name.split(" ")[1]) - 1
    cumret = cached_top10.iloc[idx]["CumReturn"]
    date_index = min(date_index, len(cumret) - 1)
    shown_dates = cumret.index[:date_index + 1]
    shown_values = cumret.values[:date_index + 1]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=shown_dates, y=shown_values,
                  mode="lines", line=dict(color="royalblue", width=3)))
    fig.update_layout(template="plotly_white",
                      title=f"Cumulative Return - {strategy_name}", height=400)
    return fig


# ================================
# 指标展示
# ================================
def plot_and_metrics(strategy_name, date_index):
    if cached_top10 is None or strategy_name is None:
        return go.Figure(), ""

    idx = int(strategy_name.split(" ")[1]) - 1
    cumret = cached_top10.iloc[idx]["CumReturn"]
    cagr = cached_top10.iloc[idx]["CAGR"]
    sharpe = cached_top10.iloc[idx]["Sharpe"]
    mdd = cached_top10.iloc[idx]["Max Drawdown"]

    date_index = min(date_index, len(cumret) - 1)
    text = (
        f"📈 Cumulative Return: {cumret.values[date_index]:.4f}\n"
        f"💰 CAGR: {cagr:.4f} | 📊 Sharpe: {sharpe:.4f} | ⚠️ MaxDD: {mdd:.4f}"
    )
    return make_plot(strategy_name, date_index), text


# ================================
# 动画函数
# ================================
def play_animation(strategy_name, current_idx, playing_state, speed):
    if cached_top10 is None or strategy_name is None:
        yield gr.update(), current_idx, False
        return

    idx = int(strategy_name.split(" ")[1]) - 1
    cumret = cached_top10.iloc[idx]["CumReturn"]

    for i in range(current_idx, len(cumret)):
        if not playing_state:
            break
        time.sleep(speed)  # 动画速度由slider控制
        yield gr.update(value=i), i, True

    yield gr.update(value=len(cumret) - 1), len(cumret) - 1, False


def stop_animation():
    return False


# ================================
# Gradio 5.x 兼容版 UI
# ================================
with gr.Blocks() as demo:
    gr.Markdown("## 💹 Quant Backtesting Dashboard (Gradio 5.x Compatible)")

    with gr.Row():
        stocks_input = gr.CheckboxGroup(stock_list, label="Select Stocks")
        step_input = gr.Slider(0.05, 0.5, value=0.25,
                               step=0.05, label="Weight Step")

    run_btn = gr.Button("🚀 Run Backtest")
    top10_table = gr.Dataframe(label="Top 10 Portfolio Strategies")

    strategy_dropdown = gr.Dropdown(label="Select Strategy")
    date_slider = gr.Slider(0, 1, step=1, label="Date Index")
    plot_out = gr.Plot(label="Cumulative Return")
    metrics_text = gr.Textbox(label="Performance Metrics", interactive=False)

    with gr.Row():
        play_btn = gr.Button("▶ Play")
        stop_btn = gr.Button("⏹ Stop")
        speed_slider = gr.Slider(
            0.05, 2.0, value=0.15, step=0.05, label="Animation Speed (sec/step)")

    playing_state = gr.State(False)
    current_index = gr.State(0)

    # ====== 新版事件系统绑定 ======
    run_btn.click(
        fn=backtest_ui,
        inputs=[stocks_input, step_input],
        outputs=[top10_table, plot_out, metrics_text,
                 strategy_dropdown, date_slider]
    )

    strategy_dropdown.change(
        fn=plot_and_metrics,
        inputs=[strategy_dropdown, date_slider],
        outputs=[plot_out, metrics_text]
    )

    date_slider.change(
        fn=plot_and_metrics,
        inputs=[strategy_dropdown, date_slider],
        outputs=[plot_out, metrics_text]
    )

    play_btn.click(
        fn=play_animation,
        inputs=[strategy_dropdown, current_index, playing_state, speed_slider],
        outputs=[date_slider, current_index, playing_state]
    )

    stop_btn.click(fn=stop_animation, outputs=[playing_state])

if __name__ == "__main__":
    demo.launch()
