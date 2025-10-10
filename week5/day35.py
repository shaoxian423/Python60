import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =============================
# 1️⃣ 模拟销售数据
# =============================
np.random.seed(42)
months = pd.date_range("2023-01-01", "2023-12-31", freq="M")
regions = ["North", "South", "East", "West"]

sales_data = []
for region in regions:
    sales = np.random.randint(5000, 15000, len(months))
    sales_data.append(pd.DataFrame({
        "Region": region,
        "Month": months,
        "Sales": sales
    }))

df_sales = pd.concat(sales_data)
df_sales["Month"] = pd.to_datetime(df_sales["Month"])
print("销售数据示例：\n", df_sales.head())

# =============================
# 2️⃣ 模拟股票数据
# =============================
dates = pd.date_range("2023-01-01", "2023-12-31", freq="B")
price = 100 + np.cumsum(np.random.normal(0, 1, len(dates)))
df_stock = pd.DataFrame({"Date": dates, "Close": price})
df_stock["Daily_Return"] = df_stock["Close"].pct_change()
df_stock["Cumulative_Return"] = (1 + df_stock["Daily_Return"]).cumprod()

# 滚动平滑（移动平均）
df_stock["Smoothed"] = df_stock["Cumulative_Return"].rolling(window=10).mean()

print("\n股票数据示例：\n", df_stock.head())

# =============================
# 3️⃣ 绘图部分
# =============================
plt.figure(figsize=(14, 10))

# (1) 每月销售趋势
plt.subplot(2, 2, 1)
for region in regions:
    region_data = df_sales[df_sales["Region"] == region]
    plt.plot(region_data["Month"], region_data["Sales"], label=region)
plt.title("📈 每月销售趋势")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

# (2) 股票累计收益率曲线
plt.subplot(2, 2, 2)
plt.plot(df_stock["Date"], df_stock["Cumulative_Return"],
         label="Cumulative Return", color='blue')
plt.plot(df_stock["Date"], df_stock["Smoothed"],
         label="Rolling Mean (10d)", color='orange', linestyle='--')
plt.title("💹 股票累计收益率曲线（含滚动平滑）")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()

# (3) 区域销售占比饼图
plt.subplot(2, 2, 3)
region_total = df_sales.groupby("Region")["Sales"].sum()
plt.pie(region_total, labels=region_total.index,
        autopct="%.1f%%", startangle=90)
plt.title("🧭 区域销售占比")

# (4) 股票波动趋势（Rolling Std）
plt.subplot(2, 2, 4)
df_stock["Volatility"] = df_stock["Daily_Return"].rolling(window=20).std()
plt.plot(df_stock["Date"], df_stock["Volatility"], color='red')
plt.title("📊 股票波动率趋势 (20日滚动标准差)")
plt.xlabel("Date")
plt.ylabel("Volatility")

plt.tight_layout()
plt.show()

# =============================
# 4️⃣ 小结输出
# =============================
print("\n🎯 项目总结：")
print("✅ 使用 Pandas 管理销售与股票两类数据")
print("✅ 结合 rolling() 实现平滑与波动率计算")
print("✅ 可视化展示业务 + 投资两种视角的数据趋势")
