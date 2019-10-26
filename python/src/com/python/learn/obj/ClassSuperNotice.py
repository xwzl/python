# 前面已经讲解了 super() 函数的用法，值得一提的是，Python 2 中 super() 函数的用法和 Python 3 大致相同，唯一的区别在于，Python 2 中不能使用零参数形式的格式，必须提供至少一个参数。
#
# 对于想要编写跨版本兼容代码的程序员来说，还要注意一件事，即 Python 2 中的 super() 函数只适用于新式类，在旧式类中不能使用 super()。
#
# 那么，什么是旧式类和新式类呢？在早期版本的 Python 中，所有类并没有一个共同的祖先 object，如果定义一个类，但没有显式指定其祖先，那么就被解释为旧式类

class OldStyle1:
    pass


class OldStyle2:
    pass


# Python 2.x 版本中，为了向后兼容保留了旧式类。该版本中的新式类必须显式继承 object 或者其他新式类
class NewStyleClass(object):
    pass


class NewStyleClassEs(NewStyleClass):
    pass


# 显然，以上两个类都属于新式类。
#
# 而在 Python 3.x 版本中，不再保留旧式类的概念。因此，没有继承任何其他类的类都隐式地继承自 object。
#
# 可以说，在 Python 3.x 中，显式声明某个类继承自 object 似乎是冗余的。但如果考虑跨版本兼容，那么就必须将 object 作为所有基类的祖先，因为如果不这么做的话，这些类
# 将被解释为旧式类，最终会导致难以诊断的问题。

# Python 中，由于基类不会在 __init__() 中被隐式地调用，需要程序员显式调用它们。这种情况下，当程序中包含多重继承的类层次结构时，使用 super 是非常危险的，往往会在类的初始化过程中出现问题。
#
# 混用super与显式类调用
#
# 分析如下程序，C 类使用了 __init__() 方法调用它的基类，会造成 B 类被调用了 2 次
class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()


class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C", end=" ")
        # super().__init__()
        # super().__init__()
        A.__init__(self)
        B.__init__(self)


print("MRO:", [x.__name__ for x in C.__mro__])
C()


class X:

    def say(self):
        print("hello X", self)


class Y:

    def say(self):
        print("hello Y", self)


class Z(X, Y):

    def say(self):
        pass


z = Z()
z.say()


# 不同种类的参数
#
# 使用 super 的另一个问题是初始化过程中的参数传递。如果没有相同的签名，一个类怎么能调用其基类的 __init__() 代码呢？这会导致下列问题
class CommonBase:
    def __init__(self):
        print("commonBase")
        super().__init__()


class Base1(CommonBase):
    def __init__(self):
        print("base1")
        super().__init__()


class Base2(CommonBase):
    def __init__(self):
        print("base2")
        super().__init__()


class MyClass(Base1, Base2):

    def __init__(self, arg):
        print("my base")
        super().__init__(arg)


MyClass(10)
