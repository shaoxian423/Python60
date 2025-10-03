# 📊 Gradio Portfolio Backtester

这个项目是一个**基于 Python 的量化回测工具**，使用 Gradio 提供交互式界面，支持股票组合策略回测和笛卡尔积策略模拟，帮助你探索不同股票组合的收益与风险。

---

## 🧩 功能特点

1. **股票组合回测**  
   - 输入股票列表和时间区间  
   - 支持不同组合规模（组合数、笛卡尔积策略）  
   - 计算关键指标：  
     - **CAGR（复合年化收益率）**  
     - **Sharpe Ratio（夏普比率）**  
     - **Max Drawdown（最大回撤）**

2. **笛卡尔积策略模拟**  
   - 系统化枚举每只股票的买入/跳过/权重组合  
   - 帮助进行 **未来策略模拟 / 风险测试 / What-If 分析**  
   - 找出高收益、高 Sharpe 的最优组合  

3. **可视化**  
   - 显示前 N 个组合的累计收益曲线  
   - 对比不同组合的收益与波动情况  

---

## ⚡ 安装依赖

```bash
pip install pandas numpy plotly gradio
🏃‍♂️ 使用方法

在 data/ 目录下准备历史价格数据 CSV，例如：

Date,AAPL,MSFT,TSLA,GOOG,AMZN
2020-01-02,72.54,94.90,67.90,152.79,28.68
2020-01-03,71.83,93.75,67.57,150.89,29.53
...


运行 Gradio 应用：

python itertools_product.py


在界面中输入：

股票列表（逗号分隔，例如 AAPL,MSFT,TSLA,GOOG,AMZN）

回测起止日期

组合规模（组合数量或笛卡尔积操作）

点击 Run Backtest

查看每个组合的 CAGR / Sharpe / Max Drawdown

前 3 个组合的累计收益曲线图

📈 示例回测结果
Action	Weights	CAGR	Sharpe	Max Drawdown
(Buy, Skip, Buy, Buy, Buy)	(0.15,0.0,0.35,0.15,0.35)	0.424	1.155	-0.507
(Skip, Skip, Buy, Buy, Buy)	(0.0,0.0,0.368,0.263,0.368)	0.430	1.152	-0.523

说明：买入 AAPL/TSLA/GOOG/AMZN 四支股票组合收益较高，但波动也大。

🔑 量化理念

CAGR：衡量年化收益速度

Sharpe Ratio：收益风险比，越高越稳健

Max Drawdown：历史最大跌幅，衡量潜在风险

量化策略核心价值：用历史数据 + 笛卡尔积/组合枚举，系统化探索所有可能操作，找到高收益、可控风险的投资方案。

📝 文件结构
project/
├─ data/
│  └─ data.csv           # 历史价格数据
├─ itertools_product.py  # Gradio 回测应用主程序
├─ backtest.py           # 回测计算函数
├─ portfolio.py          # 组合/笛卡尔积生成函数
└─ README.md             # 项目说明

⚡ 扩展方向

增加 权重优化（如均值方差优化）

添加 止损/止盈策略

接入实时行情，做 事件驱动/新闻驱动回测

增加 更多量化指标（Sortino、Calmar 等）

🛠️ 作者

Duan Shaoxian
量化策略爱好者 | Python & 数据驱动投资实践