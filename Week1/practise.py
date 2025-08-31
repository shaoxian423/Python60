# jisuanqi

a = int(input("请输入第一个数字: "))
b = int(input("请输入第二个数字: "))
print("请选择运算符:")
print("1. 加法 (+)")
print("2. 减法 (-)")
print("3. 乘法 (*)")
print("4. 除法 (/)")
choice = input("请输入运算符（1/2/3/4）: ")
if choice == '1':
    result = a + b
    print(f"{a} + {b} = {result}")
elif choice == '2':
    result = a - b
    print(f"{a} - {b} = {result}")
elif choice == '3':
    result = a * b
    print(f"{a} * {b} = {result}")
elif choice == '4':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("除数不能为零！")
else:
    print("无效的运算符选择！")

    