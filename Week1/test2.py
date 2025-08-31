
a = float(input('pls input a:'))
b = float(input('pls input b:'))

print ('''enput your choise
 1 for plus 
 2 for minus
 3 for times
 4 for divided: ''')

choice = input('Please input 1-4:')

if choice == '1':
  result = a+b 
  print(f'{a}+{b}={result}')
elif choice =='2':
  result = a-b
  print(f'{a}-{b}={result}')
elif choice =='3':
  result = a*b
  print(f'{a}*{b}={result}')
elif choice =='4':
   if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
   else:
    print("除数不能为零！")
else:
    print(f'无效选择')