# 什么是迭代器，Python迭代器及其用法
#
# 前面介绍了使用 for 循环遍历列表、元组和字典等，这些对象都是可迭代的，因此它们都属于迭代器。迭代器其实就是一个实现了迭代器协议的容器类对象。
#
# 简单的理解容器，就是用来存放各种元素的，是各种元素的集合。常用的容器包括元组、列表、字典、集合等。
#
# 迭代器基于以下两个方法实现：
#
#   __next__(self)：返回容器的下一个元素。
#   __iter__(self)：该方法返回一个迭代器（iterator）。

# 将列表转换为迭代器
my_iter = iter([2, 'fkit', 4])

# 依次获取迭代器的下一个元素
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
# print(my_iter.__next__())

# 可以看到，当遍历完序列之后如果继续遍历，会引发 StopIteration 异常，这样迭代器就可以与循环兼容，因为可以捕获这个异常并停止循环
for i in iter([2, 'fkit', 4]):
    print(i, end=" ")


# Python 也允许我们自定义一个迭代器，只需要实现 __next__() 和 __iter__() 特殊方法即可。
class CountDown:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step <= 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        return self


for element in CountDown(10):
    print(element, end=" ")


# 项目要求是这样的，定义一个类，要求在实现迭代器功能的基础上，能够对用户输入的字符串做逆序输出操作。
#
# 实现思路是这样的，自定义一个类并重载其 __init__() 初始化方法，实现为自身私有成员赋值。同时重载 __iter__() 和 __next__() 方法，
# 使其具有迭代器功能。在此基础上，如果想实现对用户输入的字符串进行逆序输出，就需要在 __next__() 方法中实现从后往前返回字符。

class Reverse:
    def __init__(self, string):
        self.__string = string
        self.__index = len(string)

    def __iter__(self):
        return self

    # 很简单，因为程序没有设置遍历的终止条件，换句话说，没有对 __index 私有变量的值对限制，这里 __index 的取值范围应为（-len(self.__index), len(self.__index)），
    # 这也是导致上面程序运行结果的根本原因。
    #
    # 编写迭代器最容易忽视的一个环节，就是在自定义类中加入对循环结束的判断，并抛出 StopIteration 异常，只有这么做了，for 循环才会接收到 StopIteration 异常，并当做终
    # 止信号来结束循环。
    def __next__(self):
        if self.__index == 0:
            raise StopIteration
        self.__index -= 1
        return self.__string[self.__index]


revstr = Reverse('Python')
for c in revstr:
    print(c, end=" ")
