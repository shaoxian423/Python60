# 动态排行榜示例

# 排行榜列表，每个元素是 (成绩, 姓名)
# 为了保持降序，分数在前面
leaderboard = [(100, "Alice"), (95, "Bob"), (90, "Charlie")]


def insert_entry(leaderboard, name, score):
    """将新成绩插入排行榜（降序）"""
    # 找到第一个比新成绩小的位置
    pos = next((i for i, (s, _) in enumerate(
        leaderboard) if s < score), len(leaderboard))
    leaderboard.insert(pos, (score, name))


def print_leaderboard(leaderboard):
    """打印排行榜"""
    print("\n当前排行榜：")
    print("----------------------------")
    print("排名 | 姓名       | 成绩")
    print("----------------------------")
    for idx, (score, name) in enumerate(leaderboard, start=1):
        print(f"{idx:>3}  | {name:<10} | {score}")
    print("----------------------------\n")


# 初始打印
print_leaderboard(leaderboard)

# 循环键盘输入
while True:
    inp = input("请输入姓名和成绩（格式: 姓名 成绩），或输入 q 退出：")
    if inp.lower() == 'q':
        print("退出程序")
        break
    try:
        name, score_str = inp.split()
        score = float(score_str)
        insert_entry(leaderboard, name, score)
        print_leaderboard(leaderboard)
    except ValueError:
        print("输入格式错误，请输入：姓名 成绩，例如：David 88")
