import json
import os

FILE_NAME = "books.json"

# 初始化书籍列表
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        # 把json文件的内容读出来,并转换成python对象(list或dict),放在内存里,下面定义的几个函数add,query和delete都是在内存里操作,只有调用save函数的时候,才会把内存里的列表写回文件.
        books = json.load(f)
        # 同时注意这个books是一个全局变量,定义在所有函数的外卖,所有函数都可以访问它(只要不在函数里用books=...重新赋值它)

else:
    books = []  # 空列表; 或空字典: books = {}; 或空集合: books = set(),这里先定义它为列表,它只是个容器,里面的元素可能是字典


def save_books():
    with open(FILE_NAME, "w") as f:  # 这段代码中用“w”打开,会清除文件里的内容
        json.dump(books, f, indent=4)  # 这段用dump,会把保存在内存里的内容都重新保存在文件里


def add_book():
    title = input("请输入书名: ")  # 这个新增变量是局部变量,只在此函数内部有效,当此函数执行完毕,这个变量就不存在了(被销毁)
    author = input("请输入作者: ")  # 同上
    year = input("请输入年份: ")  # 同上
    # 用花括号{}代表写代码是考虑到用字典类型, 这样键值配对,可用键直接访问对象,直观和方便, 也就是说把字典放在列表里注意这段代码只是用append把它加入到字典里,这时候输入的内容都保存在内存里
    books.append({"title": title, "author": author, "year": year})
    save_books()
    print("添加成功!")


def delete_book():
    title = input("请输入要删除的书名: ")
    for book in books:  # 这时的book是新定义的局部变量,叫循环变量,用来表示列表books当前便利到的元素,这个元素只在循环体内有效,循环结束后它就不再被使用了
        # 如果这个变量被找到,即和输入的书名一致的话,而且这里面的key,即title是字符串类型,因此需要加“”包起来,第二个title 本身是变量,它本身就是字符串,因此不用“”.
        if book["title"] == title:
            books.remove(book)  # 调用列表的删除方法
            save_books()
            print("删除成功!")
            # 注意这个return,它是立即结束此函数的意思,最有一句未找到该书就不会被打印(整个也可以换成if... break... else语句)
            return
            # 注意这个return的位置,当它在if缩进里的时候,条件成立会自动删除和保存文件;但当它不缩进在if(即和for并列时候)时相当于无条件退出函数了.
    print("未找到该书!")  # 这个意思是if里面遍历完没找到,就会打印此句


def query_books():
    if not books:  # 这里是没有书籍,即书籍列表为空的情况下
        print("没有书籍信息")
        return
    print("当前书籍列表:")
    # enumerate为python的内置函数,它会把列表books 遍历,同时生成索引i, 并从1开始,这是典型的for后面跟多个变量,它遍历的每个元素是序列,自动拆包,这是python中常用的元组/列表解包技巧.
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} - {book['author']} ({book['year']})")


# 主循环
while True:
    print("\n1-添加书籍  2-删除书籍  3-查看书籍  4-退出")
    choice = input("请选择操作: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        delete_book()
    elif choice == "3":
        query_books()
    elif choice == "4":
        break
    else:
        print("无效输入")
