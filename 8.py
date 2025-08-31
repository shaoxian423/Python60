print("1 -- for plus\n"
      "2 -- for minus\n"
      "3 -- for times\n"
      "4 -- for divided\n"
      "5 -- for power (a^b)\n"
      "6 -- for quit")

a = int(input("Please input a number: "))
b = int(input("Please input another number: "))

choose = int(input("Please choose operation: "))

if choose == 1:
    result = a + b
elif choose == 2:
    result = a - b
elif choose == 3:
    result = a * b
elif choose == 4:
    if b == 0:
        result = "Error: divisor cannot be 0"
    else:
        result = a / b
elif choose == 5:
    result = a ** b
else:
    result = "Invalid choice"

print("Result is:", result)

# Version 2:
