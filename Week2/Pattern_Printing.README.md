Python 字符/数字图形打印大全

本文整理了常见的图形打印方法，包括正方形、长方形、三角形、菱形、空心形状、数字金字塔等。

⸻

1. 正方形

```python
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
or:
i = 9
for i in range(9):
    print("i " * 9)

输出

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
```

⸻

2. 长方形

```python
rows = 3
cols = 7
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
or:
i = 3
for i in range(3):
    print("i " * 7)


输出

* * * * * * * 
* * * * * * * 
* * * * * * * 
```

⸻

3. 直角三角形
```python
n = 5
for i in range(1, n+1):
    print("* " * i)
or:
i = 9
for i in range(9):
    print("i " * i)

输出

* 
* * 
* * * 
* * * * 
* * * * * 
```

⸻

4. 倒直角三角形
```python
n = 5
for i in range(n, 0, -1):
    print("* " * i)

输出

* * * * * 
* * * * 
* * * 
* * 
* 
```

⸻

5. 等腰三角形（居中三角形）
```python
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)

输出

    * 
   * * 
  * * * 
 * * * * 
* * * * * 

```
⸻

6. 倒等腰三角形
```python
n = 5
for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)

输出

* * * * * 
 * * * * 
  * * * 
   * * 
    * 

```
⸻

7. 菱形

```python
n = 5
# 上半部分
for i in range(1, n+1):
    print(" " * (n-i) + "* " * i)
# 下半部分
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "* " * i)

输出

    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
```

⸻

8. 空心正方形
```python
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

输出

* * * * * 
*       * 
*       * 
*       * 
* * * * * 

```
⸻

9. 数字金字塔
```python
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + (str(i) + " ") * i)

输出

    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 

```
⸻

10. 扩展练习
	•	空心长方形：类似空心正方形，只需调整行列数。
	•	倒数字金字塔：数字递减打印。
	•	多字符图案：用不同字符打印，比如 #、$、中 等。
	•	组合图形：例如钻石、心形、箭头等，需要嵌套循环 + 条件判断。

⸻

✅ 总结思路：
	1.	外层循环 → 控制行数
	2.	内层循环或字符串重复 → 控制每行内容数量
	3.	空格 + 字符 → 控制对齐
	4.	条件判断 → 打印空心或特殊形状