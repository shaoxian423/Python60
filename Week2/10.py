def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]  # 初始化最低买入价
    max_profit = 0         # 初始化最大利润

    for price in prices:
        # 更新最低买入价
        if price < min_price:
            min_price = price
        
        # 更新最大利润
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit

# 测试
prices = [7,1,5,3,6,4]
print(max_profit(prices))  # 输出 5