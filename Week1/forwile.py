for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()
# = 1是把值赋给变量
# == 1是判断变量的值是否等于1
# != 1是判断变量的值是否不等于1
# for i in range(1, 11):i在1到10之间，range(start, stop) 的规则：
# start = 起始值（包含，inclusive)
# stop = 结束值（不包含，exclusive）
# range(1, 11) 表示 1 ≤ i < 11

# print(i) 的缩进位置决定它是否受 if 和 continue 控制，会产生三个结果：1 整个For 循环
# 结果是10，只打印了最后一个 i 的值（加上continue）；2 if 控制下，打印了奇数，这种情况下print和if是对齐的）；3 如果不加continue
# 打印了1到10的偶数。
