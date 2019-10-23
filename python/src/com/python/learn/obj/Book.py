from types import MethodType


class Book:
    book_name = None
    price = None
    author = None

    def __init__(self, book_name: str, price: float, author: str) -> None:
        self.book_name = book_name
        self.price = price
        self.author = author

    def introduction(self):
        print("%s的作者%s是一个伟大的文学家，他写的书价格都不下于%d元" % (self.book_name, self.author, self.price))


java = Book("Java 编程思想", 50.0, "高斯")
java.introduction()


# 动态绑定函数方法
def ketty(content: str):
    print(content)


java.ketty = ketty
java.ketty("nice")

# MethodType 绑定的函数与参数
java.ketty_plus = MethodType(ketty, "hello")
java.ketty_plus()


# Python 要求，类方法（构造方法和实例方法）中至少要包含一个参数，但并没有规定此参数的名称（完全可以叫任意参数名），之所以将类方法的第一个参数命名为 self，只
# 是 Python 程序员约定俗成的一种习惯，这会使程序具有更好的可读性
#
# 那么，作为类方法的第一个参数，self 参数的具体作用是什么呢？
#
# 也就是说，同一个类可以产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，换句话说，Python 会自动绑定类方法的第一个参数指
# 向调用该方法的对象。如此，Python解释器就能知道到底要操作哪个对象的方法了。
#
#    对于构造方法来说，self 参数（第一个参数）代表该构造方法正在初始化的对象。
class Dog:
    def __init__(self):
        print(self, "在调用构造方法")

    # 定义一个jump()方法
    def jump(self):
        print(self, "正在执行jump方法")

    # 定义一个run()方法，run()方法需要借助jump()方法
    def run(self):
        print(self, "正在执行run方法")
        # 使用self参数引用调用run()方法的对象
        self.jump()


dog1 = Dog()
dog1.run()
dog2 = Dog()
dog2.run()


# 需要说明的是，自动绑定的 self 参数并不依赖具体的调用方式，不管是以方法调用还是以函数调用的方式执行它，self 参数一样可以自动绑定
class User:
    def test(self):
        print('self参数: ', self)


u = User()
# 以方法形式调用test()方法
u.test()  # <__main__.User object at 0x00000000021F8240>
# 将User对象的test方法赋值给foo变量
foo = u.test
# 通过foo变量（函数形式）调用test()方法。
foo()  # <__main__.User object at 0x00000000021F8240>


# 当 self 参数作为对象的默认引用时，程序可以像访问普通变量一样来访问这个 self 参数，甚至可以把 self 参数当成实例方法的返回值。
class ReturnSelf:

    def grow(self):
        if hasattr(self, 'age'):
            self.age += 1
        else:
            self.age = 1
        # return self返回调用该方法的对象
        return self


rs = ReturnSelf()
# 可以连续调用同一个方法
rs.grow().grow().grow()
print("rs的age属性值是:", rs.age)
