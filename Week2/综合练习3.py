import json
import os
from datetime import datetime
# import tensflow
from pprint import pprint

FILE_NAME = "movies.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        movies = json.load(f)
else:
    movies = []


def save_movies():
    with open(FILE_NAME, "w")as f:
        json.dump(movies, f, indent=4)


# 这里的函数就加了参数(argu,year_str),表明要调用(callable)它的时候需要提供输入值,它是函数的行参,validate_year("2020"),这个时候2020会传递给year_str,函数内部就可以直接使用year_str了,这时2020是实参.
def validate_year(year_str):
    current_year = datetime.now().year  # 获取当前年份的数值
    if not year_str.isdigit():  # 检查它是否全部由数字组成
        return False, "Year must be a number!"
    year = int(year_str)
    if year < 1888 or year > current_year:  # First movie: 1888,等价于if 1888<= year <= current_year
        return False, f"Year must be between 1888 and {current_year}!"
    return True, year  # 注意,这个函数里有三条return!!! 第一站是数字合法,第二种是数字范围,第三种是正确.


def is_duplicate(title):  # 这就是为真的假设工具函数，如果它重复，就返回真
    for movie in movies:
        if movie["title"] == title:
            return True
    return False


def add_movies():
    title = input("please input title: ").strip()
    if not title:
        print("can not be empty")
        return
    if is_duplicate(title):
        print("movie already exist")
        return
    author = input("please input author: ").strip()
    if not author:
        print("can not be empty")
        return

    year = input("please input year: ")
    # 这里的常量year 设置成了字符串，但没关系，因为它以形参的方式马上调用了（给了）工具函数
    # 然后工具函数把它转成了整数类型。
    valid, year_of_msg = validate_year(year)
    # 这里可能不好理解，为什么用元组（两个元素）赋值一个工具函数:
    #       validate_year 返回一个元组 (valid, value_or_msg)
    #       valid 是布尔值，表示年份是否验证通过
    #       value_or_msg 如果验证成功，是整数年份；如果验证失败，是错误提示字符串
    #       用两个变量接收元组，就是“解包”元组：
    #       valid 接收第一个元素（True/False）
    #       year_of_msg 接收第二个元素（整数年份或错误信息）
    # 这样调用方可以直接通过 if not valid 来判断是否失败
    if not valid:
        print(year_of_msg)
        return
    year = year_of_msg

    movies.append({"title": title, "author": author, "year": year})
    save_movies()
    print("movies added")


def delete_movies():
    title = input("please input title you want to delete: ")
    for movie in movies:
        if movie["title"] == title:
            movies.remove(movie)
            save_movies()
            print("movie deleted")
            return
    print("not found this movie")


def query_movies():
    pprint(movies)


while True:
    print("1-for add,  2-for remove, 3-for view, 4 for exit:  ")
    choose = input("please make a choice:  ")

    if choose == "1":
        add_movies()
    elif choose == "2":
        delete_movies()
    elif choose == "3":
        query_movies()
    elif choose == "4":
        break
    else:
        print("please make a correc choice!!!")
