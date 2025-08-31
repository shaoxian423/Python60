from itertools import count, islice

numbers = islice(count(1), 100)  # 从1开始，取前100个数
print(sum(numbers))               # 输出 5050