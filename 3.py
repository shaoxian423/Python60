# 创建空字典
student_scores = {}

# 步骤1: 使用update()方法添加键值对
student_scores.update({"Alice": 85, "Bob": 92})

# 步骤2: 使用update()方法批量更新添加
student_scores.update({"Charlie": 78, "David": 95})

# 步骤3: 使用get()方法获取"Bob"的成绩，默认0，并打印
bob_score = student_scores.get("Bob", 0)
print(bob_score)

# 步骤4: 使用keys()获取所有姓名，转换为列表打印
student_names = list(student_scores.keys())
print(student_names)

# 步骤5: 使用values()获取所有成绩，计算平均值并打印
scores = list(student_scores.values())
average_score = sum(scores) / len(scores)
print(average_score)

# 步骤6: 使用items()遍历字典，打印每个学生的姓名和成绩
for name, score in student_scores.items():
    print(f"{name}: {score}")