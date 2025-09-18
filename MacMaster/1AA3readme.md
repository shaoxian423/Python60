# FinAuto – Financial Data Processing & Report Automation (1AA3 Prototype)

FinAuto is a **Python + Streamlit** prototype for financial data processing and report automation, designed to cover the core knowledge points of **McMaster University DeGroote School of Business 1AA3 Financial Accounting** course.

---

## 1AA3 Course Knowledge Summary

| Category | Knowledge Point | Description |
|----------|----------------|-------------|
| **Financial Accounting Basics** | Accounting principles | Understand core concepts such as revenue, expenses, assets, liabilities, and equity |
| **Revenue & Cost Accounting** | Revenue recognition, cost calculation | Calculate revenue, costs, and net income |
| **Assets & Liabilities Management** | Asset/liability valuation | Compute total assets, total liabilities, and shareholders’ equity |
| **Financial Statement Preparation & Analysis** | Financial statement comprehension | Generate balance sheet, income statement, and cash flow statement and analyze them |
| **Professional Ethics** | Financial reporting ethics | Ensure accurate financial data and adhere to professional standards |
| **Data Handling Skills** | Excel/Pandas/Data cleaning | Handle missing values, outliers, and duplicates to ensure data accuracy |
| **Visualization & Decision Support** | Charts & KPIs | Analyze financial data using charts for management decision support |
| **Tool Usage** | Top Hat, Excel, Python | Utilize software tools to assist learning and practice |

> **Course Focus**: Combines theory and practical skills, emphasizes quantitative financial processing, report automation, and analysis. Financial forecasting is not part of the 1AA3 curriculum.

---

## FinAuto Features & Course Knowledge Mapping

| Software Module | Feature Description | Corresponding Knowledge | Coverage |
|-----------------|------------------|-----------------------|---------|
| **Data Import** | Upload Excel/CSV files or simulate API data | Data handling skills, tool usage | ✅ Fully Covered |
| **Data Cleaning & Validation** | Check for missing values, outliers, duplicates | Data handling skills, accounting basics | ✅ Fully Covered |
| **Financial Metrics Calculation** | Compute total assets, liabilities, equity, revenue, expenses, net income, debt-to-equity, profit margin | Accounting basics, revenue & cost accounting, asset & liability management | ✅ Fully Covered |
| **Automated Report Generation** | Generate balance sheet, income statement, cash flow statement, and export to Excel | Financial statement preparation & analysis | ✅ Fully Covered |
| **Visualization & Analysis** | Bar charts, KPI dashboard, trend analysis | Visualization & decision support | ✅ Fully Covered |
| **Professional Ethics & Data Reliability** | Highlight data issues during cleaning | Professional ethics | ✅ Fully Covered |

> **Conclusion**: FinAuto fully covers the core knowledge points of 1AA3, helping students practice financial data processing, report generation, and analysis in a hands-on way.

---

## Technology Stack

- **Data Processing**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn, Plotly  
- **Report Export**: OpenPyXL  
- **Frontend**: Streamlit  

---

## Usage Instructions

1. Install dependencies:
```python
pip install streamlit pandas numpy matplotlib seaborn plotly openpyxl
```
2. Run FinAuto:
```python
streamlit run app.py
```
3. Workflow:

Data Import (Excel/CSV or simulated API)

Data Cleaning & Validation (missing values, outliers, duplicates)

Financial Metrics Calculation (revenue, costs, debt-to-equity, etc.)

Automated Report Generation (balance sheet, income statement, cash flow statement)

Visualization & Analysis (bar charts, KPI dashboard)

```python
# FinAuto – 财务数据处理与报表自动化
# 依赖: streamlit, pandas, numpy, matplotlib, seaborn, openpyxl, plotly
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from io import BytesIO

st.set_page_config(page_title="FinAuto", layout="wide")
st.title("FinAuto – 财务数据处理与报表自动化 (1AA3 原型)")

# =========================
# 1. 数据导入
# =========================
st.header("1️⃣ 数据导入")

upload_option = st.radio("选择数据导入方式:", ["上传 Excel/CSV", "模拟 API 数据"])

if upload_option == "上传 Excel/CSV":
    uploaded_file = st.file_uploader("选择 Excel/CSV 文件", type=["xlsx", "csv"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.success("数据加载成功！")
            st.dataframe(df)
        except Exception as e:
            st.error(f"读取文件失败: {e}")
else:
    st.info("模拟 API 导入数据")
    df = pd.DataFrame({
        "Name": ["Cash", "Accounts Receivable", "Inventory", "Accounts Payable", "Revenue", "Cost of Goods Sold", "Operating Expense"],
        "Category": ["Asset", "Asset", "Asset", "Liability", "Revenue", "Expense", "Expense"],
        "Balance": [5000, 3000, 2000, 2500, 10000, 4000, 1500]
    })
    st.dataframe(df)

# =========================
# 2. 数据清洗与验证
# =========================
st.header("2️⃣ 数据清洗与验证")

if 'df' in locals():
    st.subheader("数据摘要")
    st.write(df.describe(include='all'))

    # 缺失值检查
    missing_values = df.isnull().sum()
    st.write("缺失值检查:")
    st.dataframe(missing_values[missing_values > 0])

    # 重复值检查
    duplicates = df.duplicated().sum()
    st.write(f"重复条目数量: {duplicates}")

    # 异常值检测（简单: 负数余额警告）
    negative_values = df[df['Balance'] < 0]
    st.write("异常值检测（负数余额）:")
    st.dataframe(negative_values)

# =========================
# 3. 财务指标计算
# =========================
st.header("3️⃣ 财务指标计算")

if 'df' in locals():
    assets = df[df['Category'].str.lower() == 'asset']['Balance'].sum()
    liabilities = df[df['Category'].str.lower() ==
                     'liability']['Balance'].sum()
    revenue = df[df['Category'].str.lower() == 'revenue']['Balance'].sum()
    expenses = df[df['Category'].str.lower() == 'expense']['Balance'].sum()
    net_income = revenue - expenses
    equity = assets - liabilities
    debt_to_equity = liabilities / equity if equity != 0 else np.nan
    profit_margin = net_income / revenue if revenue != 0 else np.nan

    st.subheader("主要财务指标")
    st.write(f"**总资产 (Assets):** {assets}")
    st.write(f"**总负债 (Liabilities):** {liabilities}")
    st.write(f"**股东权益 (Equity):** {equity}")
    st.write(f"**净收入 (Net Income):** {net_income}")
    st.write(f"**资产负债率 (Debt-to-Equity):** {debt_to_equity:.2f}")
    st.write(f"**净利率 (Profit Margin):** {profit_margin:.2%}")

# =========================
# 4. 报表自动化生成
# =========================
st.header("4️⃣ 财务报表生成")

if 'df' in locals():
    # 资产负债表
    st.subheader("资产负债表")
    assets_df = df[df['Category'].str.lower() == 'asset']
    liabilities_df = df[df['Category'].str.lower() == 'liability']
    st.write("**资产**")
    st.dataframe(assets_df)
    st.write("**负债**")
    st.dataframe(liabilities_df)
    st.write(f"**净资产 (Assets - Liabilities):** {assets - liabilities}")

    # 利润表
    st.subheader("利润表")
    st.write(f"收入: {revenue}, 费用: {expenses}, 净收入: {net_income}")

    # 导出报表
    def to_excel(df_dict):
        output = BytesIO()
    # 使用 with 上下文，自动关闭 writer
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            for sheet_name, df_sheet in df_dict.items():
                df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)
        processed_data = output.getvalue()
        return processed_data

    excel_data = to_excel({"Balance Sheet": pd.concat([assets_df, liabilities_df]), "Income Statement": pd.DataFrame(
        {"Revenue": [revenue], "Expenses": [expenses], "Net Income": [net_income]})})
    st.download_button(label="下载 Excel 报表", data=excel_data,
                       file_name="FinAuto_Report.xlsx")

# =========================
# 5. 可视化与分析
# =========================
st.header("5️⃣ 财务可视化与分析")

if 'df' in locals():
    st.subheader("柱状图: 资产/负债/收入/费用")
    categories = ['Asset', 'Liability', 'Revenue', 'Expense']
    sums = [df[df['Category'].str.lower() == cat.lower()]['Balance'].sum()
            for cat in categories]
    fig, ax = plt.subplots()
    sns.barplot(x=categories, y=sums, palette="Set2", ax=ax)
    ax.set_ylabel("金额")
    st.pyplot(fig)

    st.subheader("KPI 仪表盘 (Plotly)")
    kpi_df = pd.DataFrame({
        "KPI": ["Assets", "Liabilities", "Equity", "Net Income", "Profit Margin"],
        "Value": [assets, liabilities, equity, net_income, profit_margin]
    })
    fig2 = px.bar(kpi_df, x="KPI", y="Value", color="KPI", text="Value")
    st.plotly_chart(fig2)

```