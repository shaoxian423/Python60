# 创建空列表
shopping_list = ["pie","egg","cake"]

# 步骤1: 使用append()添加三个物品
shopping_list.append("apple")
shopping_list.append("banana")
shopping_list.append("orange")

# 步骤2: 使用insert()在索引1位置插入"grape"
shopping_list.insert(1, "grape")

# 步骤3: 使用remove()删除第一个"banana"

shopping_list.remove("banana")
# 步骤4: 使用sort()排序（字母顺序）

shopping_list.sort()
# 步骤5: 使用reverse()反转列表

shopping_list.reverse()
# 步骤6: 打印整个列表和第二个元素（索引1）
print(shopping_list)
print(shopping_list[1])