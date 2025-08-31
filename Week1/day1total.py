import requests

# ===================== 汇率转换 =====================
def currency_converter():
    base_currency = input("请输入原始货币（如 USD、EUR、CNY）：").upper()
    target_currency = input("请输入目标货币（如 USD、EUR、CNY）：").upper()
    amount = float(input(f"请输入 {base_currency} 的金额："))
    
    url = f"https://v6.exchangerate-api.com/v6/42e07609c352e07befd0aa1c/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["result"] == "success":
            rate = data["conversion_rates"].get(target_currency)
            if rate:
                converted_amount = amount * rate
                print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            else:
                print(f"不支持的目标货币：{target_currency}")
        else:
            print("无法获取汇率数据，请检查 API 密钥或网络连接。")
    except Exception as e:
        print("获取汇率失败：", e)

# ===================== 长度单位转换 =====================
def length_converter():
    length = float(input("请输入长度数值："))
    from_unit = input("请输入原始单位（in、cm、m、ft）：").lower()
    to_unit = input("请输入目标单位（in、cm、m、ft）：").lower()
    
    conversion_factors = {
        "in": {"cm": 2.54, "m": 0.0254, "ft": 0.0833333},
        "cm": {"in": 0.393701, "m": 0.01, "ft": 0.0328084},
        "m": {"in": 39.3701, "cm": 100, "ft": 3.28084},
        "ft": {"in": 12, "cm": 30.48, "m": 0.3048}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        converted_length = length * conversion_factors[from_unit][to_unit]
        print(f"{length} {from_unit} = {converted_length:.2f} {to_unit}")
    else:
        print("不支持的单位转换。")

# ===================== 速度单位转换 =====================
def speed_converter():
    speed = float(input("请输入速度数值："))
    from_unit = input("请输入原始单位（km/h、mph）：").lower()
    to_unit = input("请输入目标单位（km/h、mph）：").lower()
    
    conversion_factors = {
        "km/h": {"mph": 0.621371},
        "mph": {"km/h": 1.60934}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        converted_speed = speed * conversion_factors[from_unit][to_unit]
        print(f"{speed} {from_unit} = {converted_speed:.2f} {to_unit}")
    else:
        print("不支持的单位转换。")

# ===================== 容量单位转换 =====================
def volume_converter():
    volume = float(input("请输入容量数值："))
    from_unit = input("请输入原始单位（gal、L）：").lower()
    to_unit = input("请输入目标单位（gal、L）：").lower()
    
    conversion_factors = {
        "gal": {"l": 3.78541},
        "l": {"gal": 0.264172}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        converted_volume = volume * conversion_factors[from_unit][to_unit]
        print(f"{volume} {from_unit} = {converted_volume:.2f} {to_unit}")
    else:
        print("不支持的单位转换。")

# ===================== 质量单位转换 =====================
def mass_converter():
    mass = float(input("请输入质量数值："))
    from_unit = input("请输入原始单位（lb、oz、kg）：").lower()
    to_unit = input("请输入目标单位（lb、oz、kg）：").lower()
    
    conversion_factors = {
        "lb": {"oz": 16, "kg": 0.453592},
        "oz": {"lb": 0.0625, "kg": 0.0283495},
        "kg": {"lb": 2.20462, "oz": 35.274}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        converted_mass = mass * conversion_factors[from_unit][to_unit]
        print(f"{mass} {from_unit} = {converted_mass:.2f} {to_unit}")
    else:
        print("不支持的单位转换。")

# ===================== 温度单位转换 =====================
def temperature_converter():
    temp = float(input("请输入温度数值："))
    from_unit = input("请输入原始单位（C、F、K）：").upper()
    to_unit = input("请输入目标单位（C、F、K）：").upper()
    
    if from_unit == "C":
        if to_unit == "F":
            converted_temp = (temp * 9/5) + 32
        elif to_unit == "K":
            converted_temp = temp + 273.15
        else:
            converted_temp = temp
    elif from_unit == "F":
        if to_unit == "C":
            converted_temp = (temp - 32) * 5/9
        elif to_unit == "K":
            converted_temp = (temp - 32) * 5/9 + 273.15
        else:
            converted_temp = temp
    elif from_unit == "K":
        if to_unit == "C":
            converted_temp = temp - 273.15
        elif to_unit == "F":
            converted_temp = (temp - 273.15) * 9/5 + 32
        else:
            converted_temp = temp
    else:
        print("不支持的温度单位。")
        return
    
    print(f"{temp} {from_unit} = {converted_temp:.2f} {to_unit}")

# ===================== 主程序 =====================
def main():
    while True:
        print("\n================== 多功能单位转换器 ==================")
        print("请选择转换类型（输入 0 退出）：")
        print("1. 汇率转换")
        print("2. 长度单位转换")
        print("3. 速度单位转换")
        print("4. 容量单位转换")
        print("5. 质量单位转换")
        print("6. 温度单位转换")
        print("======================================================")
        
        choice = input("请输入对应的数字：")
        
        if choice == "0":
            print("程序已退出，再见！")
            break
        elif choice == "1":
            currency_converter()
        elif choice == "2":
            length_converter()
        elif choice == "3":
            speed_converter()
        elif choice == "4":
            volume_converter()
        elif choice == "5":
            mass_converter()
        elif choice == "6":
            temperature_converter()
        else:
            print("无效的选择，请重新输入。")
        
        cont = input("\n是否继续？输入 1 返回选择页面，0 退出：")
        if cont == "0":
            print("程序已退出，再见！")
            break

if __name__ == "__main__":
    main()