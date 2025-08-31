while True:
    print("welcome use Temperature Conversion\n") 
    print("0---Exit")
    print("1---Temp")
    choice = input("please make choice:")
    
    if choice == "0":
        print("exit this program")
        break
    elif choice == "1":
        while True:
            try:
                temp = float(input("please input temp:"))
                break
            except:
                print("Please input a valid number !")
                continue
        from_unit = input("Original unit (C/F): ").upper()
        to_unit = input("Target unit (C/F): ").upper()

        if from_unit == "C":
            if to_unit == "F":
                convert = temp * 9/5 + 32
            else:
                convert = temp
        elif from_unit == "F":
            if to_unit == "C":
                convert = (temp - 32) * 5/9
            else:
                convert = temp
        else:
            print("Unsupported temperature unit! Only C and F are allowed.")
            continue
        print(f"{temp} {from_unit}={convert:.2f} {to_unit}")

    else :
        print("valid input,input again!")