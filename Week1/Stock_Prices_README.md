Given an array of stock prices prices, where prices[i] is the price of a given stock on the i-th day, write a function to find the maximum profit you can achieve by buying and selling the stock only once. If no profit is possible, return 0
训练点
	•	遍历数组
	•	使用变量存储最小买入价和最大利润
	•	时间复杂度 O(n)，空间复杂度 O(1)

思路解析
	1.	初始化 min_price = prices[0]，max_profit = 0
	2.	遍历每个价格 price：
	•	更新最小买入价：min_price = min(min_price, price)
	•	计算利润并更新最大利润：max_profit = max(max_profit, price - min_price)
```python
def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# 测试
prices = [7,1,5,3,6,4]
print(max_profit(prices))  # 输出 5
```

1️⃣ 一次买卖的优化写法（简洁版）

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
```
	•	与之前逻辑一致，但代码更简洁。
	•	不用 if 语句，直接用 min 和 max。
2️⃣ 可多次买卖（买卖不限次数）

如果允许 多次买卖，就可以用贪心策略，把所有上涨段的利润累加：
```python
def max_profit_multi(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit

prices = [7,1,5,3,6,4]
print(max_profit_multi(prices))  # 输出 7 (1->5 + 3->6)
```
4️⃣ 一行 Python（函数式写法）

```python
from itertools import accumulate

def max_profit(prices):
    min_prices = accumulate(prices, lambda x, y: min(x, y))
    return max(p - m for p, m in zip(prices, min_prices))
```
	•	使用 accumulate 和匿名函数，更函数式，但可读性一般。
	•	更多是展示 Python 高级用法。