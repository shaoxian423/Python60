# 🐍 Python 10周项目驱动学习计划（丰富版）

⸻

## Week 1：Python 基础与环境

📘 学习内容：
	•	Python 环境与 IDE（Anaconda / venv / pyenv）
	•	基础语法：变量、数据类型（int, float, str, bool）
	•	运算符：算术、逻辑、比较
	•	控制语句：if-else，循环（for、while）
	•	输入输出：input()、print() 格式化输出
	•	注释、代码风格（PEP 8）

📝 小项目1（综合练习）：
迷你计算器：加减乘除、平方、开方、百分比。

📝 小项目2（面试模拟）：
股票价格数组，求 最大收益区间（买入/卖出）。

### 📑 Day 1：环境搭建 & IDE
	•	安装 Python（推荐 pyenv 或 Anaconda）。
	•	学会创建虚拟环境（venv / conda）。
	•	安装 IDE：Jupyter Notebook / VS Code。
	•	用 print("Hello, Python!") 输出第一行代码。
	•	在 VS Code + Jupyter 里跑通第一个 .py 文件和 .ipynb 文件。

### 📑 Day 2：变量与数据类型
	•	学习 Python 的四种基本类型：int, float, str, bool。
	•	学会使用 type() 查看类型，str() int() float() 做类型转换。
	•	了解 Python 的动态类型特性。
##### 🔧练习：
Write a small program that takes the user’s input for name and age, and prints a  sentence. Pay attention to converting to bool:
```python
# P2.1 Get user input
name = input("Enter your name: ")
age_input = input("Enter your age: ")
# Convert age to integer
age = int(age_input)
# Example of bool conversion: check if age is positive
is_age_valid = bool(age > 0)
# Print a sentence
print(f"Hello, {name}! You are {age} years old. Age valid? {is_age_valid}")
```
#### Convert age to integer
```python
age = int(age_input)
```
#### Example of bool conversion: check if age is positive
```python
is_age_valid = bool(age > 0)
```
#### bool() 的转换规则是这样的：
	1 数值：
	•	0 → False
	•	任何非零数（比如 -1, 3.14, 100）→ True
	2 字符串:
	•	空字符串 "" → False
	•	任何非空字符串（哪怕只是 " " 一个空格，或 "hello"）→ True
    总结一句话：Python 里只要字符串不是完全空的，就认为它是真 (True)
#### list（列表）
	•	有序、可变的元素集合
	•	元素可以重复
	•	通过 索引 (index) 访问
    - * list 常用方法：
	•	append(x) → 末尾追加
	•	insert(i, x) → 指定位置插入
	•	pop(i) → 删除并返回元素 
	•	remove(x) → 删除第一个值为 x 的元素
	•	sort() → 排序
	•	reverse() → 反转
#### dict（字典）
	•	无序（Python 3.7+ 实际保持插入顺序）、可变的键值对集合
	•	键 (key) 唯一，值 (value) 可重复
	•	通过 键 (key) 访问
    - * dict 常用方法：
	•	keys() → 所有键
	•	values() → 所有值
	•	items() → 键值对 (tuple)
	•	get(key, default) → 获取值，找不到返回默认值
	•	update({...}) → 批量更新
### 📑 Day 3：运算符
	•	学习算术运算符（+ - * / // % **）。
	•	学习比较运算符（== != > < >= <=）。
	•	学习逻辑运算符（and or not）。
	•	学习赋值运算符（+=, -=, *=, /=）。
##### 🔧练习：
Let the user enter a number, and output its square, whether it is greater than 10, and whether it is even.
```python
# P 3.1
a = int(input("Please input a number: "))
# 计算平方
square = a * a
# 判断是否大于 10
greater_than_10 = square > 10
# 判断是否偶数
is_even = square % 2 == 0
# 输出结果
print(f"The square of {a} is: {square}")
print(f"Is the square greater than 10? {greater_than_10}")
print(f"Is the square even? {is_even}")
```
### 📑 Day 4：条件语句 if-else
	•	if-else 语句语法。
	•	多分支：if-elif-else。
##### 🔧练习：
	•	输入一个分数，输出成绩等级：
	•	90+ 优秀
	•	70-89 良好
	•	60-69 及格
	•	<60 不及格
```python
# P 4.1
scope = int(input("please input scope:"))
if scope >= 90:
     grade = "Excellent"
elif scope > 70:
     grade = "Good"
elif scope > 60:
     grade = "Pass"
else:
     grade = "Fail"
print(f"your grade is: {grade}")
```
### 📑 Day 5：循环 for & while
	•	for i in range(n)。
	•	while 循环。
	•	break & continue。
#### 🔧练习:
1. 9x9 multiplication table,,,Write a program to print the multiplication table from 1×1 up to 9×9.
```python
# P 5.1
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # New line after each row
```

2. Sum with while,,,Use a while loop to calculate the sum of numbers from 1 to 100.
```python
# P 5.2 Calculate sum from 1 to 100
total = 0
i = 1
while i <= 100:
    total += i
    i += 1

print(f"The sum of numbers from 1 to 100 is: {total}")
```
### 📑 Day 6：综合练习 — 迷你计算器
	•	结合 if-else、输入输出、函数。
	•	实现加、减、乘、除、开方、幂运算。
	•	进阶： 加入异常处理：不能除以 0。
#### 🔧🔧🔧综合练习:
Comprehensive Exercise — Mini Calculator
	•	Combine if-else, input/output, and functions(注意这里有函数的表述).
	•	Implement addition, subtraction, multiplication, division, square root, and exponentiation.
	•	Advanced: Add exception handling to prevent division by zero.
```python
import math

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "错误：不能除以 0！"
        return a / b
    elif op == "^":
        return a ** b
    elif op == "sqrt":
        if a < 0:
            return "错误：不能对负数开方！"
        return math.sqrt(a)
    else:
        return "错误：不支持的运算符！"

print("欢迎使用迷你计算器！")
print("支持运算: +, -, *, /, ^, sqrt")

while True:
    op = input("请输入运算符（输入 q 退出）： ")

    if op == "q":
        print("再见！")
        break

    try:
        if op == "sqrt":
            a = float(input("请输入一个数字: "))
            result = calculator(a, None, op)
        else:
            a = float(input("请输入第一个数字: "))
            b = float(input("请输入第二个数字: "))
            result = calculator(a, b, op)

        print(f"结果是: {result}")
    except ValueError:
        print("输入无效，请输入数字！")
```
注意: 这里有导入包:math,它是python自带库文件,可以实现已经封装好的计算逻辑(函数)
### Day 7：面试风格练习 — 股票最大收益
	•	问题：给定一个股票价格数组，找到最大利润（一次买入卖出）。
	•	训练点：
	•	遍历数组。
	•	变量存储最小买入价、最大利润。
#### 🔧练习：
    Best Time to Buy and Sell Stock
	•	You are given a list of stock prices where prices[i] is the price of a given stock on day i...prices = [7,1,5,3,6,4]
	•	You want to maximize your profit by choosing one day to buy and one later day to sell.
	•	Write a function that returns the maximum profit you can achieve. If no profit is possible, return 0.
训练点
	1.	遍历数组
	•	从头到尾遍历价格数组，每天判断是否能更新最小买入价或最大利润。
	2.	变量存储
	•	min_price：记录到当前为止的最低价格（潜在买入价）。
	•	max_profit：记录到当前为止能得到的最大利润。
	3.	思路总结
	•	对每一天的价格：
	1.	更新最小买入价：min_price = min(min_price, price)
	2.	计算今天卖出的利润：profit = price - min_price
	3.	更新最大利润：max_profit = max(max_profit, profit)

```python
# P 7.1
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
```

Week 2：数据结构与文件操作

📘 学习内容：
	•	数据结构：list、tuple、set、dict
	•	切片、推导式（list/dict comprehension）
	•	深拷贝 vs 浅拷贝
	•	文件操作：读写 txt、CSV、JSON
	•	异常处理：try-except-finally

📝 小项目1（综合练习）：
图书管理系统：添加/删除/查询，并保存到 JSON 文件。

📝 小项目2（面试模拟）：
读取股票历史数据 CSV，输出：
	•	最高/最低价
	•	平均收盘价
	•	波动率

⸻

Week 3：函数进阶与面向对象

📘 学习内容：
	•	函数参数（默认参数、可变参数 *args/**kwargs）
	•	Lambda、map、filter、reduce
	•	面向对象 OOP：类、对象、封装、继承、多态
	•	魔法方法（__init__, __repr__, __len__）
	•	装饰器 @decorator

📝 小项目1（综合练习）：
银行账户管理系统（支持开户、存款、取款、利息计算）。

📝 小项目2（面试模拟）：
设计一个 股票投资组合类：
	•	添加/删除股票
	•	计算总市值、收益率
	•	支持多种货币（汇率转换）

⸻

Week 4：模块、库与工具

📘 学习内容：
	•	Python 内置模块：os, sys, math, random, datetime
	•	collections（Counter, defaultdict, deque）
	•	itertools（组合、排列、笛卡尔积）
	•	functools（partial, lru_cache）
	•	虚拟环境与依赖管理（pip, requirements.txt, poetry）

📝 小项目1（综合练习）：
随机密码生成器（支持字母/数字/特殊符号）。

📝 小项目2（面试模拟）：
写函数：输入交易日日期（含节假日），返回 下一个交易日（考察 datetime & 金融应用）。

⸻

Week 5：Pandas 数据分析基础

📘 学习内容：
	•	Pandas 数据结构：Series, DataFrame
	•	导入数据（CSV, Excel, JSON, SQL）
	•	数据清洗：缺失值处理、重复值去除
	•	统计分析：均值、中位数、方差、相关性
	•	分组聚合：groupby, pivot_table

📝 小项目1（综合练习）：
销售数据分析：
	•	每月总销售额
	•	最畅销商品
	•	客户购买频率

📝 小项目2（面试模拟）：
股票 CSV → 计算：
	•	日收益率
	•	累计收益率曲线
	•	波动率（标准差）

⸻

Week 6：数据可视化

📘 学习内容：
	•	matplotlib：折线图、柱状图、散点图
	•	seaborn：分布图、热力图
	•	图表美化：标题、标签、图例、颜色
	•	双轴图、子图
	•	交互式可视化：plotly

📝 小项目1（综合练习）：
绘制 销售额趋势图 + 热力图。

📝 小项目2（面试模拟）：
绘制 股票价格 K 线图，叠加 移动平均线。

⸻

Week 7：爬虫与数据获取

📘 学习内容：
	•	requests 请求网页/API
	•	BeautifulSoup 解析 HTML
	•	JSON 数据解析
	•	爬虫异常处理与重试
	•	API 调用：Alpha Vantage / Yahoo Finance

📝 小项目1（综合练习）：
爬取新闻标题，保存到 CSV。

📝 小项目2（面试模拟）：
调用金融 API，获取股票数据并绘制趋势图。

⸻

Week 8：算法与数据结构应用

📘 学习内容：
	•	常见算法：排序、查找、二分法
	•	数据结构：栈、队列、堆、链表
	•	动态规划（DP）入门
	•	时间复杂度 Big-O

📝 小项目1（综合练习）：
实现一个 排序工具（支持冒泡、快速排序）。

📝 小项目2（面试模拟）：
经典题：
连续子数组最大和（Kadane 算法，动态规划）。

⸻

Week 9：机器学习基础

📘 学习内容：
	•	机器学习流程（数据 → 训练 → 测试 → 评估）
	•	监督学习：线性回归、逻辑回归、KNN
	•	模型评估：MSE、准确率、混淆矩阵
	•	scikit-learn 基本用法

📝 小项目1（综合练习）：
波士顿房价预测（线性回归）。

📝 小项目2（面试模拟）：
股票二分类预测（明日涨/跌）。

⸻

Week 10：综合项目 & 模拟面试

📘 学习内容：
	•	项目模块化
	•	单元测试（pytest/unittest）
	•	调试（pdb, logging）
	•	代码优化与面试模拟

📝 小项目1（综合练习）：
个人理财助手：
	•	输入支出/收入
	•	输出收支统计与趋势图

📝 小项目2（面试模拟）：
金融数据面试题：
	•	给定股票/基金数据，计算 最大回撤、夏普比率、收益率
	•	输出结果并可视化
