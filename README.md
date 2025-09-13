# 🐍 Python QiQi 和她爹的Python基地（丰富版）10周
![商科学生技能雷达图](Pics/Skills_Radar_Chart.png)
- [🐍 Python QiQi 和她爹的Python基地（丰富版）10周](#-python-qiqi-和她爹的python基地丰富版10周)
	- [Week 1：Python 基础与环境](#week-1python-基础与环境)
		- [📑 Day 1：环境搭建 \& IDE](#-day-1环境搭建--ide)
		- [📑 Day 2：变量与数据类型](#-day-2变量与数据类型)
			- [🔧练习：](#练习)
		- [📑 Day 3：运算符](#-day-3运算符)
			- [🔧练习：](#练习-1)
		- [📑 Day 4：条件语句 if-else](#-day-4条件语句-if-else)
			- [🔧练习：](#练习-2)
		- [📑 Day 5：循环 for \& while](#-day-5循环-for--while)
			- [🔧练习:](#练习-3)
		- [📑 Day 6：综合练习 — 迷你计算器](#-day-6综合练习--迷你计算器)
			- [🔧🔧综合练习1: Mini Calculator(具体请看Week1子目录下的CalcluaterREADME)](#综合练习1-mini-calculator具体请看week1子目录下的calcluaterreadme)
		- [📑 Day 7 ：面试模拟  小项目2— 股票最大收益：](#-day-7-面试模拟--小项目2-股票最大收益)
			- [🔧🔧综合练习2：Best Time to Buy and Sell Stock,(具体请看Week1子目录下的Stock)](#综合练习2best-time-to-buy-and-sell-stock具体请看week1子目录下的stock)
	- [Week 2：数据结构与文件操作](#week-2数据结构与文件操作)
		- [数据结构学习内容：](#数据结构学习内容)
		- [📑 Day 8：list（列表）基础](#-day-8list列表基础)
			- [🔧练习：创建一个 list，增加、插入、删除元素，并排序输出。](#练习创建一个-list增加插入删除元素并排序输出)
		- [📑 Day 9：tuple（元组）基础](#-day-9tuple元组基础)
			- [🔧练习：创建一个 tuple，统计元素出现次数，并查找索引。](#练习创建一个-tuple统计元素出现次数并查找索引)
		- [📑 Day 10：set（集合）基础](#-day-10set集合基础)
			- [🔧练习：创建两个 set，并进行集合运算。](#练习创建两个-set并进行集合运算)
		- [📑 Day 11：dict（字典）基础](#-day-11dict字典基础)
			- [🔧练习：创建一个字典，访问、更新和遍历元素。](#练习创建一个字典访问更新和遍历元素)
		- [📑 Day 12：切片与推导式](#-day-12切片与推导式)
			- [🔧练习：使用切片和推导式创建新的 list。](#练习使用切片和推导式创建新的-list)
		- [📑 Day 13：深拷贝 vs 浅拷贝](#-day-13深拷贝-vs-浅拷贝)
			- [🔧练习：演示浅拷贝和深拷贝的不同。](#练习演示浅拷贝和深拷贝的不同)
		- [📑 Day 14：文件操作与异常处理](#-day-14文件操作与异常处理)
			- [🔧练习：读取 txt 文件并捕获异常。](#练习读取-txt-文件并捕获异常)
			- [🔧🔧综合练习1:  Library Management System with JSON Persistence：](#综合练习1--library-management-system-with-json-persistence)
			- [🔧🔧综合练习2:（面试模拟）Stock Data Analysis:CSV Reader with Statistics and Volatility：](#综合练习2面试模拟stock-data-analysiscsv-reader-with-statistics-and-volatility)
			- [🔧🔧综合练习3: Advanced Movie Collection Manager with JSON Persistence](#综合练习3-advanced-movie-collection-manager-with-json-persistence)
				- [Title and Director cannot be empty](#title-and-director-cannot-be-empty)
				- [Release Year must be a number between 1888 and the current year](#release-year-must-be-a-number-between-1888-and-the-current-year)
				- [Prevent duplicate titles (case-insensitive)](#prevent-duplicate-titles-case-insensitive)
				- [Genre is optional; default to "Unknown" if left blank](#genre-is-optional-default-to-unknown-if-left-blank)
				- [Users can delete by title (case-insensitive) or index number in the list](#users-can-delete-by-title-case-insensitive-or-index-number-in-the-list)
				- [Sort movies by Release Year](#sort-movies-by-release-year)
	- [Week 3：函数进阶与面向对象](#week-3函数进阶与面向对象)
		- [📑 Day 15: 函数基础](#-day-15-函数基础)
		- [📑 Day 16: 函数进阶与作用域](#-day-16-函数进阶与作用域)
		- [📑 Day 17: 模块与包](#-day-17-模块与包)
		- [📑 Day 18: 文件操作](#-day-18-文件操作)
		- [📑 Day 19: 异常处理](#-day-19-异常处理)
		- [📑 Day 20: OOP 基础](#-day-20-oop-基础)
		- [📑 Day 21: OOP 进阶](#-day-21-oop-进阶)

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
#### 🔧练习：
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
Convert age to integer
```python
age = int(age_input)
```
Example of bool conversion: check if age is positive
```python
is_age_valid = bool(age > 0)
```
bool() 的转换规则是这样的：
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
#### 🔧练习：
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
#### 🔧练习：
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
![alt text](Pics/ifelse.png)
### 📑 Day 5：循环 for & while
	•	for i in range(n)。
	•	while 循环。
	•	break & continue。
#### 🔧练习:
1. 9x9 multiplication table,,,Write a program to print the multiplication table from 1×1 up to 9×9.
```python
# P 5.1
for i in range(1, 10): # rows 是外循环来控制
    for j in range(1, i+1): # clus 是内循环来控制
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
![alt text](Pics/forwhile.png)
### 📑 Day 6：综合练习 — 迷你计算器
	•	结合 if-else、输入输出、函数。
	•	实现加、减、乘、除、开方、幂运算。
	•	进阶： 加入异常处理：不能除以 0。
#### 🔧🔧综合练习1: Mini Calculator(具体请看Week1子目录下的CalcluaterREADME)
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
### 📑 Day 7 ：面试模拟  小项目2— 股票最大收益：
股票价格数组，求 最大收益区间（买入/卖出）。
	•	问题：给定一个股票价格数组，找到最大利润（一次买入卖出）。
	•	训练点：
	•	遍历数组。
	•	变量存储最小买入价、最大利润。
#### 🔧🔧综合练习2：Best Time to Buy and Sell Stock,(具体请看Week1子目录下的Stock)
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
# 弹出,注意这里是定义了popped,因此可以打印,但如果不定义的话可以直接用fruis.pop()
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
numbers = (1, 2, 3, 2, 4, 2) # 注意tuple用(),而list用[],而且count() 和 index() 都可以用在 有序序列（list 或 tuple）上,他们是这两种序列的方法。count是计数,计算它出现的次数,而index是它索引的位置.
# tuple 之所以经常提到这些方法，是因为它 不可变，你无法用 append/remove 之类修改它，所以这些只读方法就显得尤为重要。
count_2 = numbers.count(2)
index_3 = numbers.index(3)
print("Tuple:", numbers)
print("Count of 2:", count_2)
print("Index of 3:", index_3)
```
### 📑 Day 10：set（集合）基础
	•	学习 set 的无序性、可变性和唯一性。
	•	掌握集合运算：交集、并集、差集、对称差集。
	•	学会使用 add(), remove(), discard(), pop() 方法。

#### 🔧练习：创建两个 set，并进行集合运算。
```python
# P10.1 Set操作练习,非空集合可以用 {},空集合必须用 set(),可以用 set() 将 list、tuple、字符串等可迭代对象转换为集合.
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
### 📑 Day 11：dict（字典）基础
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
for key, value in student.items(): # 注意这里定义的两个循环变量:key和value,这种写法就可以自动拆包,如果是for key in student呢?就是只用一个变量呢?结果会是什么样子?
    print(key, ":", value)
```
### 📑 Day 12：切片与推导式
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
### 📑 Day 13：深拷贝 vs 浅拷贝
	•	理解浅拷贝 (shallow copy) 与深拷贝 (deep copy) 的区别。
	•	学会使用 copy() 和 deepcopy()。
	•	了解嵌套列表复制的注意点。

#### 🔧练习：演示浅拷贝和深拷贝的不同。
```python
# P13.1
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print("Original:", original)
print("Shallow copy:", shallow) # 浅copy = 外层分家,内层同居,一旦改变b的内层将会影响a的内层
print("Deep copy:", deep)  # 深copy = 外层分家,内层也分家,一旦改变b的内层不会影响a的内层
# P13.2
import copy
a = [1,2 [3, 4]]
b = copy.copy(a) # shallow copy

print(a) #[1, 2, [3, 4]]
print(b) #[1, 2, [3, 4]]

b[0] = 99
print(a) #[1, 2, [3, 4]]
print(b) #[99, 2, [3, 4]] 外层数据分开了

b[2][0] = 77 # b的第二个元素(0,1,2)的第零个元素被新赋值为77
print(a) = #[1, 2, [77, 4]] 它的内层被修改了
print(b) = #99, 2, [77, 4]]

# P13.3
a = [1,2 [3, 4]]
c = copy.deepcopy(a) # deep copy

c[0] = 99
c[2][0] = 77

print(a) # [1, 2, [3, 4]] 外层完全不受影响
print(c) # [99,2, [77, 4]]
```
### 📑 Day 14：文件操作与异常处理
	•	学习文件读写 txt、CSV、JSON。
	•	掌握异常处理 try-except-finally。
	•	了解文件操作中的常见错误及处理方法。

#### 🔧练习：读取 txt 文件并捕获异常。
```python
# P14.1 文件操作练习
try: # try表示“尝试执行下面的执行块, 如果出错,会转到except
    with open("example.txt", "r") as f: # 表示以只读模式(r) 打开example.txt, Ms.ariana 请注意:
		# 每个文件都分为很多种模式,对于系统文件,大部分都为只读文件,对于公开文件,都为可修改模式. r = read only
		# with...as f是上下文管理器:保证文件用完后自动关闭,即使中途出错也会执行f.close().
        content = f.read() # 读取整个文件内容,返回字符串,并保存到content变量里,
        print("File content:", content)
except FileNotFoundError: # 如果这个文件不存在,就会捕获这个错误并执行里面的代码,这样做的好处(此处的逻辑)是避免程序直接崩溃
    print("File not found!")
finally: # 无论是否出错,finally里的代码都会执行
    print("Execution finished.")
```

#### 🔧🔧综合练习1:  Library Management System with JSON Persistence：
建立一个图书管理系统：能添加/删除/查询，并保存到 JSON 文件。
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
        books = json.load(f) # 把json文件的内容读出来,并转换成python对象(list或dict),放在内存里,下面定义的几个函数add,query和delete都是在内存里操作,只有调用save函数的时候,才会把内存里的列表写回文件.
		# 同时注意这个books是一个全局变量,定义在所有函数的外卖,所有函数都可以访问它(只要不在函数里用books=...重新赋值它)

else:
    books = [] # 空列表; 或空字典: books = {}; 或空集合: books = set(),这里先定义它为列表,它只是个容器,里面的元素可能是字典

def save_books():
    with open(FILE_NAME, "w") as f: # 这段代码中用“w”打开,会清除文件里的内容
        json.dump(books, f, indent=4) # 这段用dump,会把保存在内存里的内容都重新保存在文件里

def add_book():
    title = input("请输入书名: ") # 这个新增变量是局部变量,只在此函数内部有效,当此函数执行完毕,这个变量就不存在了(被销毁)
    author = input("请输入作者: ") # 同上
    year = input("请输入年份: ") # 同上
    books.append({"title": title, "author": author, "year": year}) # 用花括号{}代表写代码是考虑到用字典类型, 这样键值配对,可用键直接访问对象,直观和方便, 也就是说把字典放在列表里注意这段代码只是用append把它加入到字典里,这时候输入的内容都保存在内存里
    save_books()
    print("添加成功!")

def delete_book():
    title = input("请输入要删除的书名: ")
    for book in books: # 这时的book是新定义的局部变量,叫循环变量,用来表示列表books当前便利到的元素,这个元素只在循环体内有效,循环结束后它就不再被使用了
        if book["title"] == title: # 如果这个变量被找到,即和输入的书名一致的话,而且这里面的key,即title是字符串类型,因此需要加“”包起来,第二个title 本身是变量,它本身就是字符串,因此不用“”.
            books.remove(book) #调用列表的删除方法
            save_books()
            print("删除成功!")
            return # 注意这个return,它是立即结束此函数的意思,最有一句未找到该书就不会被打印(整个也可以换成if... break... else语句)
			#注意这个return的位置,当它在if缩进里的时候,条件成立会自动删除和保存文件;但当它不缩进在if(即和for并列时候)时相当于无条件退出函数了.
    print("未找到该书!") # 这个意思是if里面遍历完没找到,就会打印此句

def query_books():
    if not books: # 这里是没有书籍,即书籍列表为空的情况下
        print("没有书籍信息")
        return  
    print("当前书籍列表:")
    for i, book in enumerate(books, start=1): # enumerate为python的内置函数,它会把列表books 遍历,同时生成索引i, 并从1开始,这是典型的for后面跟多个变量,它遍历的每个元素是序列,自动拆包,这是python中常用的元组/列表解包技巧.
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
注意: 运行此程序的时候,会提示你添加docstring,要分清注释(#)和文档字符串(docstring)之间的区别:
docstring是同时给人和机器看的,可通过help()或.__doc__获取;# 只是给人看的.

#### 🔧🔧综合练习2:（面试模拟）Stock Data Analysis:CSV Reader with Statistics and Volatility：
build a small program that reads historical stock data from a CSV file and computer basic statistics
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
#### 🔧🔧综合练习3: Advanced Movie Collection Manager with JSON Persistence
Objective:
Build a movie collection management system that allows users to add, delete, view, and search movies, with data stored persistently in a JSON file. The system should include input validation and prevent duplicate entries.
Functional Requirements:
Add a movie
Fields: Title, Director, Release Year, Genre
Validation:
##### Title and Director cannot be empty
##### Release Year must be a number between 1888 and the current year
##### Prevent duplicate titles (case-insensitive)
##### Genre is optional; default to "Unknown" if left blank
Delete a movie
##### Users can delete by title (case-insensitive) or index number in the list
Print a message if the movie is not found
View movies
Display all movies in a readable JSON-like format
##### Sort movies by Release Year
Search movies (optional challenge)
Allow filtering by title, director, or year
Data persistence
All movie data must be saved in a JSON file
On program start, load existing data so the collection persists between sessions
Extra Challenge (Optional)
Improve user experience with pretty-printing
Allow partial search (e.g., searching for "Star" finds "Star Wars")
Prevent invalid input for all fields
Starter Hints
Use the json module to read/write JSON files
Use os.path.exists() to check if the JSON file exists
Validate user input before saving
Use json.dumps(..., indent=4) to display movies neatly
```python
import json
import os
from datetime import datetime

FILE_NAME = "movies.json"

# Load existing movie data or create empty list
if os.path.exists(FILE_NAME):
	with open(FILE_NAME, "r") as f:
		movies = json.load(f)
else:
	movies = []

# Save movies to JSON
def save_movies():
	with open(FILE_NAME, "w") as f:
		json.dump(movies, f, indent=4, ensure_ascii=False)

# Validate year
def validate_year(year_str): # 这里的函数就加了参数(argu,year_str),表明要调用(callable)它的时候需要提供输入值,它是函数的行参,validate_year("2020"),这个时候2020会传递给year_str,函数内部就可以直接使用year_str了,这时2020是实参.
	current_year = datetime.now().year # 获取当前年份的数值
	if not year_str.isdigit():# 检查它是否全部由数字组成
		return False, "Year must be a number!"# 
	year = int(year_str)
	if year < 1888 or year > current_year:  # First movie: 1888,等价于if 1888<= year <= current_year
		return False, f"Year must be between 1888 and {current_year}!"
	return True, year # 注意,这个函数里有三条return!!! 第一站是数字合法,第二种是数字范围,第三种是正确.

# Check for duplicate title
def is_duplicate(title):
	for movie in movies:
		if movie["title"].lower() == title.lower():
			return True
	return False

# Add a movie
def add_movie():
	title = input("Enter movie title: ").strip()
	if not title:
		print("Title cannot be empty!")
		return
	if is_duplicate(title):
		print("This movie already exists in the collection!")
		return
	
	director = input("Enter director name: ").strip()
	if not director:
		print("Director cannot be empty!")
		return
	
	year_input = input("Enter release year: ").strip()
	valid, year_or_msg = validate_year(year_input)
	if not valid:
		print(year_or_msg)
		return
	year = year_or_msg
	
	genre = input("Enter genre: ").strip()
	if not genre:
		genre = "Unknown"
	
	movies.append({
		"title": title,
		"director": director,
		"year": year,
		"genre": genre
	})
	save_movies()
	print("Movie added successfully!")

# Delete a movie
def delete_movie():
	if not movies:
		print("No movies to delete.")
		return

	print("Current movies:")
	for i, m in enumerate(movies):
		print(f"{i+1}. {m['title']} ({m['year']})")
	
	choice = input("Enter movie title or index to delete: ").strip()
	if choice.isdigit():
		index = int(choice) - 1
		if 0 <= index < len(movies):
			removed = movies.pop(index)
			save_movies()
			print(f"Removed movie: {removed['title']}")
			return
		else:
			print("Invalid index!")
			return
	
	# Delete by title
	for movie in movies:
		if movie["title"].lower() == choice.lower():
			movies.remove(movie)
			save_movies()
			print(f"Removed movie: {movie['title']}")
			return
	
	print("Movie not found!")

# Query movies
def query_movies():
	if not movies:
		print("No movies in the collection.")
		return
	# Sort by year before displaying
	sorted_movies = sorted(movies, key=lambda x: x["year"])
	print(json.dumps(sorted_movies, indent=4, ensure_ascii=False))

# Main loop
while True:
	print("\n1 - Add movie, 2 - Delete movie, 3 - View movies, 4 - Exit")
	choice = input("Enter your choice: ").strip()
	
	if choice == "1":
		add_movie()
	elif choice == "2":
		delete_movie()
	elif choice == "3":
		query_movies()
	elif choice == "4":
		print("Exiting program. Bye!")
		break
	else:
		print("Invalid choice, try again!")
```

## Week 3：函数进阶与面向对象

📘 学习内容：
	•	函数参数（默认参数、可变参数 *args/**kwargs）
	•	Lambda、map、filter、reduce
	•	面向对象 OOP：类、对象、封装、继承、多态
	•	魔法方法（__init__, __repr__, __len__）
	•	装饰器 @decorator
### 📑 Day 15: 函数基础
	•	定义函数
	•	返回值:
	•	函数参数类型:位置参数,关键字参数,默认参数,可变阐述 *args/**kwargs
### 📑 Day 16: 函数进阶与作用域
	•	局部变量 VS 全局变量
	•	global 与 nonlocal
	•	匿名函数: lambda
	•	高阶函数: map(),filter(),reduce(),sorted(),zip()
### 📑 Day 17: 模块与包
	•	模块导入: import module/from module import func
	•	常用标准库: math,random,datetime,os,sys
	•	自定义模块: 创建.py文件并导入
### 📑 Day 18: 文件操作
	•	打开文件: open(‘file.txt’,mode)
	•	文件模式: r,w,a,rb,wb
	•	读取方法: read(),deadline(),readlines()
	•	写入方法: write(),writelines()
	•	使用 with 自动关闭文件: 
### 📑 Day 19: 异常处理
	•	try...except...finally
	•	捕获特定异常
	•	自定义异常
### 📑 Day 20: OOP 基础
	•	类和对象:class className:
	•	属性与方法
	•	构造方法: __init__
	•	实例化对象
### 📑 Day 21: OOP 进阶
	•	继承与多态
	•	方法重写
	•	super()
	•	类属性与实例属性
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
