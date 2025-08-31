import requests

while True:
    print("Welcome to use DUAN converter!\n")
    print("===== Multi function Converter =====")
    print("Please select conversion type (input number):")
    print("0 - Exit")
    print("1 - Currency Converter")
    print("2 - Length Converter")
    print("3 - Speed Converter")
    print("4 - Volume Converter")   
    print("5 - Mass Converter")
    print("6 - Temperature Converter")

    choice = input("select your choice: ")

    if choice == "0":
        print("Program exited.")
        break

    elif choice == "1":
         base = input("Please enter base currency (e.g., USD, EUR, CNY): ").upper()
         target = input("Please enter target currency (e.g., USD, EUR, CNY): ").upper()
         try:
             amount = float(input(f"Please enter amount in {base}: "))
         except:
          print("请输入有效数字！")
          continue
         
         url = f“”