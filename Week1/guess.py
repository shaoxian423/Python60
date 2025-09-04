import random


def guess_number():
    # 计算机随机生成一个1~100的整数
    number_to_guess = random.randint(1, 10)
    print("欢迎来到猜数字游戏！我已经选择了一个 1 到 100 的数字。")

    while True:
        user_input = input("请输入你的猜测（数字）：")

        # 判断输入是否为数字
        if not user_input.isdigit():
            print("请输入一个有效的数字！")
            continue

        user_guess = int(user_input)

        # 判断猜测结果
        if user_guess < number_to_guess:
            print("太小了，再试一次！")
        elif user_guess > number_to_guess:
            print("太大了，再试一次！")
        else:
            print(f"恭喜你，猜对了！答案就是 {number_to_guess}。")
            break


# 运行游戏
if __name__ == "__main__":
    guess_number()
