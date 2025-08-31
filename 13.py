import tkinter as tk
import math

def calculate():
    try:
        expr = entry.get()  # 从输入框获取表达式
        result = eval(expr, {"__builtins__": None}, {"math": math})
        label.config(text=f"结果: {result}")
    except Exception as e:
        label.config(text=f"错误: {e}")

root = tk.Tk()
root.title("迷你计算器")

# 输入框
entry = tk.Entry(root, width=20, font=("Arial", 14))
entry.pack(pady=10)

# 按钮
button = tk.Button(root, text="计算", command=calculate, font=("Arial", 12))
button.pack(pady=5)

# 结果标签
label = tk.Label(root, text="结果: ", font=("Arial", 14))
label.pack(pady=10)

root.mainloop()