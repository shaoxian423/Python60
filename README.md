# 🐍 Python 10周项目学习计划 ---QiQi 和她爹的Python基地（丰富版）

⸻

## Week 1：Python 基础与环境

📘 学习内容：
	•	Python 环境与 IDE（Anaconda / venv / pyenv）
	•	基础语法：变量、数据类型（int, float, str, bool）
	•	运算符：算术、逻辑、比较
	•	控制语句：if-else，循环（for、while）
	•	输入输出：input()、print() 格式化输出
	•	注释、代码风格（PEP 8）

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
for i in range(1, 10): # rows 是外循环来控制
    for j in range(1, i+1): # clos 是内循环来控制
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
#### 🔧🔧🔧 📝 综合练习: 小项目1：
迷你计算器：加减乘除、平方、开方、百分比。
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
### Day 7 📝：面试模拟  小项目2— 股票最大收益：
股票价格数组，求 最大收益区间（买入/卖出）。
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

## Week 2：数据结构与文件操作
### 数据结构学习内容：
	•	数据结构：list、tuple、set、dict
	•	切片、推导式（list/dict comprehension）
	•	深拷贝 vs 浅拷贝
	•	文件操作：读写 txt、CSV、JSON
	•	异常处理：try-except-finally
```python
list（列表）
	•	有序、可变的元素集合
	•	元素可以重复
	•	通过索引 (index) 访问
list 常用方法：
	•	append(x) → 末尾追加
	•	insert(i, x) → 指定位置插入
	•	pop(i) → 删除并返回元素
	•	remove(x) → 删除第一个值为 x 的元素
	•	sort() → 排序
	•	reverse() → 反转
tuple（元组）
	•	有序、不可变的元素集合
	•	元素可以重复
	•	通过索引 (index) 访问
	•	常用于存储固定的数据，比如函数返回多个值
tuple 常用操作/方法：
	•	count(x) → 统计元素 x 出现次数
	•	index(x) → 返回元素 x 第一次出现的位置
注意：元组不可变，不能使用 append(), remove() 等修改方法
set（集合）
	•	无序、可变的元素集合
	•	元素唯一，重复元素会自动去重
	•	支持集合运算：交集、并集、差集、对称差集
set 常用方法：
	•	add(x) → 添加元素 x
	•	remove(x) → 删除元素 x（不存在会报错）
	•	discard(x) → 删除元素 x（不存在不会报错）
	•	pop() → 随机删除并返回一个元素
	•	union(other_set) → 并集
	•	intersection(other_set) → 交集
	•	difference(other_set) → 差集
	•	symmetric_difference(other_set) → 对称差集
dict（字典）
	•	无序（Python 3.7+ 实际保持插入顺序）、可变的键值对集合
	•	键 (key) 唯一，值 (value) 可重复
	•	通过键 (key) 访问
dict 常用方法：
	•	keys() → 所有键
	•	values() → 所有值
	•	items() → 键值对 (tuple)
	•	get(key, default) → 获取值，找不到返回默认值
	•	update({...}) → 批量更新
类型对比表
类型	有序	可变	元素唯一	索引访问	 常用场景
list	✅		✅		❌		✅		 可变列表、栈/队列
tuple	✅		❌		❌		✅		 固定数据、函数返回值
set		❌		✅		✅		❌		 去重、集合运算
dict	❌		✅		键唯一	通过 key	键值映射
```
### 📑 Day 8：list（列表）基础
	•	学习 list 的有序性、可变性和重复元素特性。
	•	学会通过索引访问元素。
	•	掌握 append(), insert(), pop(), remove(), sort(), reverse() 方法。

#### 🔧练习：创建一个 list，增加、插入、删除元素，并排序输出。
```python
# P8.1 List操作练习
fruits = ["apple", "banana", "cherry"]
# 追加
fruits.append("orange")
# 插入
fruits.insert(1, "grape")
# 删除
fruits.remove("banana")
# 弹出
popped = fruits.pop(2)
# 排序
fruits.sort()
# 输出结果
print("Fruits:", fruits)
print("Popped element:", popped)
```
### 📑 Day 9：tuple（元组）基础
	•	学习 tuple 的有序性、不可变性和重复元素特性。
	•	通过索引访问元素。
	•	掌握 count(), index() 方法。
	•	了解 tuple 常用于固定数据或函数返回多个值。
#### 🔧练习：创建一个 tuple，统计元素出现次数，并查找索引。
```python
# P9.1 Tuple练习
numbers = (1, 2, 3, 2, 4, 2)
count_2 = numbers.count(2)
index_3 = numbers.index(3)
print("Tuple:", numbers)
print("Count of 2:", count_2)
print("Index of 3:", index_3)
```
## 📑 Day 10：set（集合）基础
	•	学习 set 的无序性、可变性和唯一性。
	•	掌握集合运算：交集、并集、差集、对称差集。
	•	学会使用 add(), remove(), discard(), pop() 方法。

#### 🔧练习：创建两个 set，并进行集合运算。
```python
# P10.1 Set操作练习
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# 添加元素
a.add(5)
# 删除元素
a.remove(2)
# 并集
union_set = a.union(b)
# 交集
intersection_set = a.intersection(b)
# 差集
diff_set = a.difference(b)
print("Set a:", a)
print("Set b:", b)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", diff_set)
```
## 📑 Day 11：dict（字典）基础
	•	学习 dict 的键唯一、值可重复、可变特性。
	•	通过 key 访问元素。
	•	掌握 keys(), values(), items(), get(), update() 方法。

#### 🔧练习：创建一个字典，访问、更新和遍历元素。
```python
# P11.1 Dict操作练习
student = {"name": "Alice", "age": 20, "major": "CS"}
# 获取值
age = student.get("age")
# 更新
student.update({"age": 21, "grade": "A"})
# 遍历
for key, value in student.items():
    print(key, ":", value)
```
## 📑 Day 12：切片与推导式
	•	学习 list、tuple 的切片方法。
	•	学习 list/dict comprehension。
	•	了解推导式在创建新集合中的优势。

#### 🔧练习：使用切片和推导式创建新的 list。
```python
# P12.1 切片与推导式
numbers = [0, 1, 2, 3, 4, 5, 6]
# 切片
slice_numbers = numbers[2:6]
# list comprehension
squares = [x*x for x in numbers if x%2==0]
print("Slice:", slice_numbers)
print("Squares of even numbers:", squares)
```
## 📑 Day 13：深拷贝 vs 浅拷贝
	•	理解浅拷贝 (shallow copy) 与深拷贝 (deep copy) 的区别。
	•	学会使用 copy() 和 deepcopy()。
	•	了解嵌套列表复制的注意点。

#### 🔧练习：演示浅拷贝和深拷贝的不同。
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)
```
## 📑 Day 14：文件操作与异常处理
	•	学习文件读写 txt、CSV、JSON。
	•	掌握异常处理 try-except-finally。
	•	了解文件操作中的常见错误及处理方法。

#### 🔧练习：读取 txt 文件并捕获异常。
```python
# P14.1 文件操作练习
try:
    with open("example.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution finished.")
```


📝 小项目1（综合练习）：
图书管理系统：添加/删除/查询，并保存到 JSON 文件。
功能点：
	1.	添加书籍（书名、作者、年份）。
	2.	删除书籍（通过书名或索引）。
	3.	查询书籍（查看全部或按书名搜索）。
	4.	数据保存到 JSON 文件，下次打开仍能读取。
```python
import json
import os

FILE_NAME = "books.json"

# 初始化书籍列表
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        books = json.load(f)
else:
    books = []

def save_books():
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)

def add_book():
    title = input("请输入书名: ")
    author = input("请输入作者: ")
    year = input("请输入年份: ")
    books.append({"title": title, "author": author, "year": year})
    save_books()
    print("添加成功!")

def delete_book():
    title = input("请输入要删除的书名: ")
    for book in books:
        if book["title"] == title:
            books.remove(book)
            save_books()
            print("删除成功!")
            return
    print("未找到该书!")

def query_books():
    if not books:
        print("没有书籍信息")
        return
    print("当前书籍列表:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} - {book['author']} ({book['year']})")

# 主循环
while True:
    print("\n1-添加书籍  2-删除书籍  3-查看书籍  4-退出")
    choice = input("请选择操作: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        query_books()
    elif choice == "4":
        break
    else:
        print("无效输入")
```
📝 小项目2（面试模拟）：
读取股票历史数据 CSV，输出：
	•	最高/最低价
	•	平均收盘价
	•	波动率
功能点：
	1.	读取 CSV（包含 Date、Open、High、Low、Close）。
	2.	输出最高价、最低价、平均收盘价。
	3.	计算波动率（通常用收盘价的标准差 / 平均值）。

示例代码：
```python
import pandas as pd

# 读取 CSV 文件
file_name = "stock_data.csv"  # CSV 文件应包含 Date, Open, High, Low, Close
df = pd.read_csv(file_name)

# 输出最高价和最低价
highest = df['High'].max()
lowest = df['Low'].min()
print(f"最高价: {highest}, 最低价: {lowest}")

# 平均收盘价
avg_close = df['Close'].mean()
print(f"平均收盘价: {avg_close:.2f}")

# 波动率: 收盘价标准差 / 平均值
volatility = df['Close'].std() / avg_close
print(f"波动率: {volatility:.2%}")
```
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
