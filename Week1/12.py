import requests

while True:
    print("\n===== 多功能命令行转换器 =====")
    print("请选择转换类型（输入数字）：")
    print("0 - 退出")
    print("1 - 汇率转换")
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


    elif choice == "6":
        # 温度转换（只支持 C 和 F）
        while True:
            try:
                temp = float(input("请输入温度数值："))
                break
            except:
                print("请输入有效数字！")
                continue
        from_unit = input("原单位（C/F）：").upper()
        to_unit = input("目标单位（C/F）：").upper()

        if from_unit == "C":
            if to_unit == "F":
                converted = temp * 9/5 + 32
            else:  # C->C
                converted = temp
        elif from_unit == "F":
            if to_unit == "C":
                converted = (temp - 32) * 5/9
            else:  # F->F
                converted = temp
        else:
            print("不支持的温度单位！仅支持 C 和 F")
            continue

        print(f"{temp} {from_unit} = {converted:.2f} {to_unit}")

    else:
        print("无效选择，请重新输入。")