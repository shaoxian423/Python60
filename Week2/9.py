import math  # 用于开方 sqrt

# 定义计算函数
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
    elif op == "^":  # 幂运算
        return a ** b
    elif op == "sqrt":  # 开方，只用 a
        if a < 0:
            return "错误：不能对负数开方！"
        return math.sqrt(a)
    else:
        return "错误：不支持的运算符！"

# 主程序
print("欢迎使用迷你计算器！")
print("支持运算: +, -, *, /, ^, sqrt")

while True:
    op = input("请输入运算符（输入 q 退出）： ")

    if op == "q":  # 退出程序
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