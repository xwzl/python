# global 关键字用于全局变量同名参数被遮蔽的情况，nonlocal 用于局部变量同名参数被遮蔽的情况
from builtins import print

book = "Java 入门到放弃"


def bookShop():
    # 全局变量被遮蔽
    global book
    print(book)
    book = "Go 入门到放弃"

    book_name = "书名"

    def bookNames():
        # 避免局部变量被遮蔽
        nonlocal book_name
        print(book_name)
        book_name = "作者"

    bookNames()

    print("hello")


bookShop()
