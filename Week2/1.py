import json
import os

FILE_NAME = "books.json"

# 初始化书籍列表
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        books = json.load(f)
else:
    books = []


def save_books():
    with open(FILE_NAME, "w") as f:
        json.dump(books, f, indent=4)


def add_book():
    title = input("请输入书名: ")
    author = input("请输入作者: ")
    year = input("请输入年份: ")
    books.append({"title": title, "author": author, "year": year})
    save_books()
    print("添加成功!")


def delete_book():
    title = input("请输入要删除的书名: ")
    for book in books:
        if book["title"] == title:
            books.remove(book)
            save_books()
            print("删除成功!")
            return
    print("未找到该书!")


def query_books():
    if not books:
        print("没有书籍信息")
        return
    print("当前书籍列表:")
    # enumberate是枚举器的意思,就是在遍历可迭代对象的时候,同时拿到元素的索引和值
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} - {book['author']} ({book['year']})")


# 主循环
while True:
    print("\n1-添加书籍  2-删除书籍  3-查看书籍  4-退出")
    choice = input("请选择操作: ")
    if choice == "1":  # 必须用“”把数字括起来,因为用户输入的是数字,必须把它变成字符串再来比较,或用.strip()
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        query_books()
    elif choice == "4":
        break
    else:
        print("无效输入")
