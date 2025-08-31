# fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) / 1.8
# print(f"The temperature in Celsius is: {celsius:.2f}")
# print(f"The temperature in Celsius is: {round(celsius)}") # Rounds to nearest integer
# print(f"The temperature in Celsius is: {int(celsius)}") # Truncates decimal part,PaT: compare the round
# print(f"The temperature in Celsius is: {celsius:.4f}") # Displays four decimal places
# print(f"The temperature in Celsius is: {celsius:.0f}") # Rounds to nearest integer, no decimal places
# print(f"The temperature in Celsius is: {celsius:.1f}") # Displays one decimal place

import requests

while True:
    print("\n===== 多功能命令行转换器 =====")
    print("请选择转换类型（输入数字）：")
    print("0 - 退出")
    print("1 - 汇率转换")
    print("2 - 长度转换")
    print("3 - 速度转换")
    print("4 - 容量转换")
    print("5 - 质量转换")
    print("6 - 温度转换")

    choice = input("请输入选择：")

    if choice == "0":
        print("程序已退出。")
        break

    elif choice == "1":
        # 汇率转换
        base = input("请输入原始货币（如 USD、EUR、CNY）：").upper()
        target = input("请输入目标货币（如 USD、EUR、CNY）：").upper()
        try:
            amount = float(input(f"请输入 {base} 的金额："))
        except:
            print("请输入有效数字！")
            continue

        url = f"https://v6.exchangerate-api.com/v6/42e07609c352e07befd0aa1c/latest/{base}"
        try:
            data = requests.get(url).json()
            if data["result"] == "success":
                rate = data["conversion_rates"].get(target)
                if rate:
                    print(f"{amount} {base} = {amount*rate:.2f} {target}")
                else:
                    print(f"不支持的目标货币：{target}")
            else:
                print("无法获取汇率数据，请检查 API 或网络。")
        except Exception as e:
            print("获取汇率失败：", e)

    elif choice == "2":
        # 长度转换
        try:
            length = float(input("请输入长度数值："))
        except:
            print("请输入有效数字！")
            continue
        from_unit = input("原单位（in/cm/m/ft）：").lower()
        to_unit = input("目标单位（in/cm/m/ft）：").lower()
        factors = {
            "in":{"cm":2.54,"m":0.0254,"ft":0.0833333},
            "cm":{"in":0.393701,"m":0.01,"ft":0.0328084},
            "m":{"in":39.3701,"cm":100,"ft":3.28084},
            "ft":{"in":12,"cm":30.48,"m":0.3048}
        }
        try:
            converted = length * factors[from_unit][to_unit]
            print(f"{length} {from_unit} = {converted:.4f} {to_unit}")
        except:
            print("不支持的单位转换。")

    elif choice == "3":
        # 速度转换
        try:
            speed = float(input("请输入速度数值："))
        except:
            print("请输入有效数字！")
            continue
        from_unit = input("原单位（km/h/mph）：").lower()
        to_unit = input("目标单位（km/h/mph）：").lower()
        factors = {"km/h":{"mph":0.621371},"mph":{"km/h":1.60934}}
        try:
            converted = speed * factors[from_unit][to_unit]
            print(f"{speed} {from_unit} = {converted:.4f} {to_unit}")
        except:
            print("不支持的单位转换。")

    elif choice == "4":
        # 容量转换
        try:
            vol = float(input("请输入容量数值："))
        except:
            print("请输入有效数字！")
            continue
        from_unit = input("原单位（gal/L）：").lower()
        to_unit = input("目标单位（gal/L）：").lower()
        factors = {"gal":{"l":3.78541},"l":{"gal":0.264172}}
        try:
            converted = vol * factors[from_unit][to_unit]
            print(f"{vol} {from_unit} = {converted:.4f} {to_unit}")
        except:
            print("不支持的单位转换。")

    elif choice == "5":
        # 质量转换
        try:
            mass = float(input("请输入质量数值："))
        except:
            print("请输入有效数字！")
            continue
        from_unit = input("原单位（lb/oz/kg）：").lower()
        to_unit = input("目标单位（lb/oz/kg）：").lower()
        factors = {
            "lb":{"oz":16,"kg":0.453592},
            "oz":{"lb":0.0625,"kg":0.0283495},
            "kg":{"lb":2.20462,"oz":35.274}
        }
        try:
            converted = mass * factors[from_unit][to_unit]
            print(f"{mass} {from_unit} = {converted:.4f} {to_unit}")
        except:
            print("不支持的单位转换。")

    elif choice == "6":
        # 温度转换
        try:
            temp = float(input("请输入温度数值："))
        except:
            print("请输入有效数字！")
            continue
        from_unit = input("原单位（C/F/K）：").upper()
        to_unit = input("目标单位（C/F/K）：").upper()
        if from_unit=="C":
            if to_unit=="F": converted = temp*9/5+32
            elif to_unit=="K": converted = temp+273.15
            else: converted = temp
        elif from_unit=="F":
            if to_unit=="C": converted = (temp-32)*5/9
            elif to_unit=="K": converted = (temp-32)*5/9+273.15
            else: converted = temp
        elif from_unit=="K":
            if to_unit=="C": converted = temp-273.15
            elif to_unit=="F": converted = (temp-273.15)*9/5+32
            else: converted = temp
        else:
            print("不支持的温度单位！")
            continue
        print(f"{temp} {from_unit} = {converted:.2f} {to_unit}")

    else:
        print("无效选择，请重新输入。")